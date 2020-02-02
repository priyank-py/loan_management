from django.shortcuts import render
from .models import Expense
from django.db.models import Sum
from datetime import date, datetime
from django.http import HttpResponse
import calendar
import csv

# Create your views here.

def upcomming_expenses(request):
    pass

def expenses(request):
    current_month = int(datetime.now().strftime('%m'))
    current_month_word = datetime.now().strftime('%B')
    current_year = int(datetime.now().strftime('%Y'))
    first_day, last_day = calendar.monthrange(current_year, current_month)
    start_month_date = datetime.today().replace(day=1)
    end_month_date = datetime.today().replace(day=last_day)
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')
    
    
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()  
    except:
        start_date = start_month_date
    try:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date() 
    except:
        end_date = end_month_date

    all_expenses = Expense.objects.all().filter(budget__date__gte=start_date).filter(budget__date__lte=end_date)
    # all_expenses_budget = [i.budget.date for i in all_expenses]
    
    paid = [i.installments.aggregate(Sum('amount_paid'))['amount_paid__sum'] if i.installments.exists() else 0 for i in all_expenses]
    to_pay = [i.budget.amount - j if i.installments.exists() else i.budget.amount for i, j in zip(all_expenses, paid)]
    pay_for = [i.budget.title for i in all_expenses]
    # expense_data = list(zip(all_expenses, paid, to_pay))
    
    start_end = f'{start_date.strftime("%m-%d-%Y")}_{end_date.strftime("%m-%d-%Y")}'

    context = {
        'pay_for': pay_for,
        'paid': paid,
        'to_pay': to_pay,
        # 'expense_data': expense_data,
        'start_end': start_end,
    }
    return render(request, 'expense/expenses.html', context)


def download_expenses(request, start_end):
    start_date, end_date = start_end.split('_')
    current_month = int(datetime.now().strftime('%m'))
    current_month_word = datetime.now().strftime('%B')
    current_year = int(datetime.now().strftime('%Y'))
    first_day, last_day = calendar.monthrange(current_year, current_month)
    start_month_date = datetime.today().replace(day=1)
    end_month_date = datetime.today().replace(day=last_day)

    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%d').date()  
    except:
        start_date = start_month_date
    try:
        end_date = datetime.strptime(end_date, '%Y-%m-%d').date() 
    except:
        end_date = end_month_date

    all_expenses = Expense.objects.all().filter(budget__date__gte=start_date).filter(budget__date__lte=end_date)

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="expenses {start_end}.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Budget', 'Vendor', 'Budget Type', 'Expense Type', 'Vendor', 'Remarks', 
                    'Paid Amt (Installment 1)', 'Date', 'Payment Method', 'Cheque/Transaction/Card/DD number', 'Pay Status',
                    'Paid Amt (Installment 2)', 'Date', 'Payment Method', 'Cheque/Transaction/Card/DD number', 'Pay Status',
                    'Paid Amt (Installment 3)', 'Date', 'Payment Method', 'Cheque/Transaction/Card/DD number', 'Pay Status',
                    'Paid Amt (Installment 4)', 'Date', 'Payment Method', 'Cheque/Transaction/Card/DD number', 'Pay Status',
                    'Paid Amt (Installment 5)', 'Date', 'Payment Method', 'Cheque/Transaction/Card/DD number', 'Pay Status',
                    ])
    
    for expense in all_expenses:
        
        expense_list = [expense.id, expense.budget.title, expense.vendor.name, expense.budget.budget_type, expense.expense_type, expense.vendor.name, expense.purpose]
        if expense.installments.exists():
            for installment in expense.installments.all():
                expense_list.append(installment.amount_paid)
                expense_list.append(installment.date)
                expense_list.append(installment.payment_method)
                expense_list.append(installment.transaction_no)
                expense_list.append(installment.payed)
            
        writer.writerow(expense_list)
       

    # if any(all_budgets):
    #     for budget in all_budgets:
    #         writer.writerow([budget.id, budget.title, budget.amount, budget.date, budget.budget_type, budget.vendor.name])
    # else:
    #     writer.writerow(['','','','','',''])
    return response