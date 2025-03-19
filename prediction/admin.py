from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_approved']
    list_filter = ['is_approved']
    actions = ['approve_doctors']

    def approve_doctors(self, request, queryset):
        queryset.update(is_approved=True)
