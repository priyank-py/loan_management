from django.shortcuts import render
from .models import Budget
from datetime import date, datetime
import calendar
from django.http import HttpResponse
import csv
# Create your views here.

def create_budget(request):
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

    all_budgets = Budget.objects.all().filter(date__gte=start_date).filter(date__lte=end_date)
    print(all_budgets)
    budget_label = [i.title for i in all_budgets]
    amount = [i.amount for i in all_budgets]
    print(amount)


    start_end = f'{start_date.strftime("%m-%d-%Y")}_{end_date.strftime("%m-%d-%Y")}'
    print(start_end)
    context = {
        'current_month_word': current_month_word,
        'current_year': current_year,
        'budget_label': budget_label,
        'amount': amount,
        'start_end': start_end,
    }

    return render(request, 'budget/index.html', context)



def download_csv(request, start_end):
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

    all_budgets = Budget.objects.all().filter(date__gte=start_date).filter(date__lte=end_date)

    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="budget {start_end}.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Title', 'Amount', 'Date', 'Budget Type','Vendor'])
    
    if any(all_budgets):
        for budget in all_budgets:
            writer.writerow([budget.id, budget.title, budget.amount, budget.date, budget.budget_type, budget.vendor.name])
    else:
        writer.writerow(['','','','','',''])
    return response