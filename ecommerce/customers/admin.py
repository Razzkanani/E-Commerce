from django.contrib import admin
from .models import Customer

admin.site.register(Customer)

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'contact_number', 'email']