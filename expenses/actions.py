# import unicodecsv
# from django.http import HttpResponse

# def export_as_csv_action(description="Export selected objects as CSV file",
#                          fields=None, exclude=None, header=True):
#     """
#     This function returns an export csv action
#     'fields' and 'exclude' work like in django ModelForm
#     'header' is whether or not to output the column names as the first row
#     """
#     def export_as_csv(modeladmin, request, queryset):
#         opts = modeladmin.model._meta
        
#         if not fields:
#             field_names = [field.name for field in opts.fields]
#         else:
#             field_names = fields

#         response = HttpResponse(content_type ='text/csv')
#         response['Content-Disposition'] = 'attachment; filename=%s.csv' % (str(opts).replace('.', '_'))

#         writer = unicodecsv.writer(response, encoding='utf-8')
#         if header:
#             writer.writerow(field_names)
#         for obj in queryset:
#             row = [getattr(obj, field)() if callable(getattr(obj, field)) else getattr(obj, field) for field in field_names]
#             writer.writerow(row)
#         return response
#     export_as_csv.short_description = description
#     return export_as_csv


import csv
from collections import OrderedDict
from functools import wraps

from django.db.models import FieldDoesNotExist
from django.http import HttpResponse

from singledispatch import singledispatch  # pip install singledispatch


def prep_field(obj, field):
    """
    (for download_as_csv action)
    Returns the field as a unicode string. If the field is a callable, it
    attempts to call it first, without arguments.
    """
    if '__' in field:
        bits = field.split('__')
        field = bits.pop()

        for bit in bits:
            obj = getattr(obj, bit, None)

            if obj is None:
                return ""

    attr = getattr(obj, field)
    output = attr() if callable(attr) else attr
    return unicode(output).encode('utf-8') if output is not None else ""


@singledispatch
def download_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.

    Example:

        class ExampleModelAdmin(admin.ModelAdmin):
            raw_id_fields = ('field1',)
            list_display = ('field1', 'field2', 'field3',)
            actions = [download_as_csv,]
            download_as_csv_fields = [
                'field1',
                ('foreign_key1__foreign_key2__name', 'label2'),
                ('field3', 'label3'),
            ],
            download_as_csv_header = True
    """
    fields = getattr(modeladmin, 'download_as_csv_fields', None)
    exclude = getattr(modeladmin, 'download_as_csv_exclude', None)
    header = getattr(modeladmin, 'download_as_csv_header', True)
    verbose_names = getattr(modeladmin, 'download_as_csv_verbose_names', True)

    opts = modeladmin.model._meta

    def fname(field):
        if verbose_names:
            return unicode(field.verbose_name).capitalize()
        else:
            return field.name

    # field_names is a map of {field lookup path: field label}
    if exclude:
        field_names = OrderedDict(
            (f.name, fname(f)) for f in opts.fields if f not in exclude
        )
    elif fields:
        field_names = OrderedDict()
        for spec in fields:
            if isinstance(spec, (list, tuple)):
                field_names[spec[0]] = spec[1]
            else:
                try:
                    f, _, _, _ = opts.get_field_by_name(spec)
                except FieldDoesNotExist:
                    field_names[spec] = spec
                else:
                    field_names[spec] = fname(f)
    else:
        field_names = OrderedDict(
            (f.name, fname(f)) for f in opts.fields
        )

    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % (
            unicode(opts).replace('.', '_')
        )

    writer = csv.writer(response)

    if header:
        writer.writerow(field_names.values())

    for obj in queryset:
        writer.writerow([prep_field(obj, field) for field in field_names.keys()])
    return response

download_as_csv.short_description = "Download selected objects as CSV file"


@download_as_csv.register(str)
def _(description):
    """
    (overridden dispatcher)
    Factory function for making a action with custom description.

    Example:

        class ExampleModelAdmin(admin.ModelAdmin):
            raw_id_fields = ('field1',)
            list_display = ('field1', 'field2', 'field3',)
            actions = [download_as_csv("Export Special Report"),]
            download_as_csv_fields = [
                'field1',
                ('foreign_key1__foreign_key2__name', 'label2'),
                ('field3', 'label3'),
            ],
            download_as_csv_header = True
    """
    @wraps(download_as_csv)
    def wrapped_action(modeladmin, request, queryset):
        return download_as_csv(modeladmin, request, queryset)
    wrapped_action.short_description = description
    return wrapped_action