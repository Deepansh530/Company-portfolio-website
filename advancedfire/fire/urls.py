# fire/urls.py (app-level)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staff/', views.staff_list, name='staff_list'),
    path('staff/<slug:slug>/', views.staff_detail, name='staff_detail'),
]
