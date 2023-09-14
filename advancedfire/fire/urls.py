# fire/urls.py (app-level)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('team/', views.staff_list, name='staff_list'),  # Add a name for this URL pattern
    path('team/<slug:slug>/', views.staff_detail, name='staff_detail'),
]
