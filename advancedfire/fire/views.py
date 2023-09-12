# fire/views.py

from django.shortcuts import render, get_object_or_404
from .models import Staff

def home(request):
    return render(request, 'fire/home.html')

def staff_list(request):
    staff_members = Staff.objects.all()
    return render(request, 'fire/staff/our-staff.html', {'staff_members': staff_members})

def staff_detail(request, slug):
    staff_member = get_object_or_404(Staff, slug=slug)
    return render(request, 'fire/staff/staff-detail.html', {'staff_member': staff_member})
