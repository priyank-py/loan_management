from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_budget, name="create_budget"),
    path('download_budget/<str:start_end>', views.download_csv, name="download_budget")
]
