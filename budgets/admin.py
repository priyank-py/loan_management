from django.contrib import admin
from .models import Budget

# Register your models here.

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'date','vendor', 'budget_type']
    list_display_links = ['title', 'amount', 'date']
    list_filter = ('budget_type', 'vendor', 'date', )
    search_fields = ['title', 'vendor', 'date', 'budget_type']
    # actions = [export_as_csv_action("CSV Export", fields=['id', 'title', 'date', 'vendor', 'budget_type']),]
    