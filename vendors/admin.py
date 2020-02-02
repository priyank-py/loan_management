from django.contrib import admin
from .models import Vendor, VendorAccount

# Register your models here.

class VendorAccountInline(admin.TabularInline):
    model = VendorAccount
    extra = 1


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'connection']
    search_fields = ['name', 'phone', 'connection']
    list_display_links =  ['name', 'phone',]
    inlines = (VendorAccountInline,)

    
