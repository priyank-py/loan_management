from django.shortcuts import render
from .models import Vendor
from expenses.models import Expense
from budgets.models import Budget
from django.db.models import Sum
import datetime

# Create your views here.

def profile(request):

    all_vendors = Vendor.objects.all()

    budget_vendor = [Budget.objects.all().filter(vendor=i).aggregate(Sum('amount'))['amount__sum'] for i in all_vendors]
    expense_vendor = [sum([j.installments.aggregate(Sum('amount_paid'))['amount_paid__sum'] for j in Expense.objects.all().filter(vendor=i)]) for i in all_vendors]
    last_paid_on = [sorted([j.installments.last().date if j.installments.exists() else None for j in Expense.objects.all().filter(vendor=i)], reverse=True)[0] if Expense.objects.all().filter(vendor=i).exists() else None for i in all_vendors]
    pay_percent = [round(((i-j)/i)*100) if not i == None else 0 for i, j in zip(budget_vendor, expense_vendor)]
    print(budget_vendor)
    print(expense_vendor)
    print(last_paid_on)
    vendor_data = list(zip(all_vendors, pay_percent, last_paid_on))

    context = {
        'vendor_data': vendor_data
    }

    return render(request, 'vendor/profile.html', context)
