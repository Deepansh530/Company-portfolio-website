from django.contrib import admin
from .models import Staff
from .models import Review

# Register your models here.
admin.site.register(Staff)
admin.site.register(Review)