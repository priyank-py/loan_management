from django.urls import path
from . import views 

urlpatterns = [
    path('upcomming', views.upcomming_expenses, name="upcomming_expenses"),
    path('', views.expenses, name="expense"),
    path('expense/<str:start_end>', views.download_expenses, name="download_expenses")
]
