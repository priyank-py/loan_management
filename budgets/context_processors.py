
from .models import Budget
from datetime import date, timedelta


def notification(request):
    
    seven_days = timedelta(days=7)
    

    new_budget = Budget.objects.all().filter(date__gte=date.today()).filter(date__lte=date.today()+seven_days)
    notification_no = new_budget.count()
    
    return {'new_budget': new_budget, 'notification_no': notification_no,}

