from django.shortcuts import render
from budgets.models import Budget
from expenses.models import Expense
import calendar 
from datetime import datetime, date, timedelta
from django.db.models import Sum
import json


def dashboard(request):

    current_month = int(datetime.now().strftime('%m'))
    current_month_word = datetime.now().strftime('%B')
    current_year = int(datetime.now().strftime('%Y'))
    first_day, last_day = calendar.monthrange(current_year, current_month)
    start_month_date = datetime.today().replace(day=1)
    end_month_date = datetime.today().replace(day=last_day)
    months_budget = Budget.objects.all().filter(date__gte=start_month_date).filter(date__lte=end_month_date)
    total_month = Budget.objects.all().filter(date__gte=start_month_date).filter(date__lte=end_month_date).aggregate(Sum('amount'))

    budget_next_seven_days = Budget.objects.all().filter(date__gte=date.today()).filter(date__lte=date.today() + timedelta(days=6)).aggregate(Sum('amount'))

    months_budgets_id = [i.id for i in months_budget]

    expenses_this_month = Expense.objects.all().filter(installments__date__gte=start_month_date).filter(installments__date__lte=date.today())

    expenses_so_far = Expense.objects.all().filter(installments__date__gte=start_month_date).filter(installments__date__lte=date.today()).values_list('installments__amount_paid')

    expenses_so_far = sum([sum(i) for i in expenses_so_far])
    print(expenses_so_far)
    expenses_past_seven_days = Expense.objects.all().filter(installments__date__gte=date.today() - timedelta(days=6)).filter(installments__date__lte=date.today()).values_list('installments__amount_paid')
    expenses_past_seven_days = sum([sum(i) for i in expenses_past_seven_days])

    if len(expenses_this_month) > 5:
        all_incomplete = {i:[i.installments.aggregate(Sum('amount_paid')), round(((i.budget.amount - i.installments.aggregate(Sum('amount_paid'))['amount_paid__sum'])/i.budget.amount)*100), i.installments.last().next_pay_date] for i in expenses_this_month.order_by('-budget__amount')[:5]}
    else:
        all_incomplete = {i:[i.installments.aggregate(Sum('amount_paid')), round(((i.budget.amount - i.installments.aggregate(Sum('amount_paid'))['amount_paid__sum'])/i.budget.amount)*100), i.installments.last().next_pay_date] for i in expenses_this_month.order_by('-budget__amount')}
    print(all_incomplete)

    #For graph

    expense_per_budget = [{i: [i.title, i.amount,Expense.objects.all().filter(budget=i)[0].installments.aggregate(Sum('amount_paid'))]} if Expense.objects.all().filter(budget=i).exists() else {i:[i.title, i.amount, 0]} for i in months_budget ]
    print(expense_per_budget)

    budget_labels = [i.title for i in months_budget]
    budget_amount = [i.amount for i in months_budget]
    budget_expense = [Expense.objects.all().filter(budget=i)[0].installments.aggregate(Sum('amount_paid'))['amount_paid__sum'] if Expense.objects.all().filter(budget=i).exists() else 0  for i in months_budget]

    context = {
        'current_month_word':current_month_word, 
        'current_year': current_year,
        'months_budget': months_budget,
        'total_month': total_month,
        'budget_next_seven_days': budget_next_seven_days,
        'expenses_so_far': expenses_so_far,
        'expenses_so_far': expenses_so_far,
        'expenses_past_seven_days': expenses_past_seven_days,
        'all_incomplete': all_incomplete,
        'budget_labels': budget_labels,
        'budget_amount': budget_amount,
        'budget_expense': budget_expense,
    }

    return render(request, 'main/index.html', context)

