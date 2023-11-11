from django.contrib import admin
from .models import Customer, Installation, Order, Technician

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Installation)
class InstallationAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['installation', 'date_created', 'date_updated']

@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    pass
