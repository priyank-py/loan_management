from django.contrib import admin
from .models import Expense, ExpenseInstallment
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
from django.http import HttpResponse, HttpResponseForbidden
from import_export.admin import ImportExportModelAdmin

# from .actions import export_as_csv_action
# Register your models here.

class ExpenseInstallmentInline(admin.TabularInline):
    model = ExpenseInstallment
    extra = 1


# class ExpenseResource(resources.ModelResource):
#     expense = fields.Field(
#         column_name = 'budget',
#         attribute = 'installments',
#         widget = ForeignKeyWidget(ExpenseInstallment, 'amount_paid')
#     )


@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):

    def get_date(self, instance):
        try:
            return instance.installments.last().date
        except:
            return None
    
    def get_installment_dates(self, instance):
        try:
            return instance.installments.last().date
        except:
            return None
    



    list_display = ['budget', 'purpose','vendor']
    list_display_links =  ['budget', 'purpose','vendor']
    list_filter = [('installments__date', DateRangeFilter),'purpose', 'vendor']

    inlines = (ExpenseInstallmentInline,)
    # resource_class = ExpenseResource
    # actions = [export_as_csv_action("CSV Export", fields=['id', 'budget', 'vendor', 'purpose', 'installments__date'])]
    # actions = [download_as_csv,]

    # def export_as_csv(self, request, queryset):

    #     meta = self.model._meta
        
    #     self.save_as = True
    #     field_names = [field.name for field in meta.fields] + ['installments__date', 'installments__amount_paid']
    #     print(field_names)

    #     response = HttpResponse(content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    #     writer = csv.writer(response)

    #     writer.writerow(field_names)
    #     for obj in queryset:
    #         row = writer.writerow([getattr(obj, field) for field in field_names])

    #     return response

    # export_as_csv.short_description = "Export Selected as csv"

    # download_as_csv_fields = [
    #     'id', 'budget', 'vendor'
    #     ('installments__amount_paid'),
    #     ('purpose',),
    # ],
    # download_as_csv_header = True

      
    
    
