from django.contrib import admin
from .models import Customer, CustomerType, Plan, DeviceList, ONU, Router, Mininode, DelayedReason, DROP, Installation, InstallationCategory, InstallationType, KardexDROP, KardexTensioners, Technician, Municipality


@admin.register(Municipality)
class MunicipalityAdmin(admin.ModelAdmin):
    pass


@admin.register(Technician)
class TechnicianAdmin(admin.ModelAdmin):
    pass


@admin.register(KardexTensioners)
class KardexTensionersAdmin(admin.ModelAdmin):
    pass


@admin.register(KardexDROP)
class KardexDROPAdmin(admin.ModelAdmin):
    pass


@admin.register(InstallationType)
class InstallationTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(InstallationCategory)
class InstallationCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DROP)
class DROPAdmin(admin.ModelAdmin):
    pass


@admin.register(DelayedReason)
class DelayedReasonAdmin(admin.ModelAdmin):
    pass


@admin.register(Mininode)
class MininodeAdmin(admin.ModelAdmin):
    pass

# @admin.register(Installation)
# class InstallationAdmin(admin.ModelAdmin):
#     pass

class InstallationInline(admin.StackedInline):
    model = Installation


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [InstallationInline]


@admin.register(CustomerType)
class CustomerTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass


@admin.register(DeviceList)
class DeviceListAdmin(admin.ModelAdmin):
    pass


@admin.register(ONU)
class ONUAdmin(admin.ModelAdmin):
    pass


@admin.register(Router)
class RouterAdmin(admin.ModelAdmin):
    pass







