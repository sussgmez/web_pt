import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords



class Technician(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Usuario"), on_delete=models.CASCADE)
    document = models.IntegerField(_("Nro. De Cédula"))
    phone_1 = models.CharField(_("Teléfono 1"), max_length=20)
    phone_2 = models.CharField(_("Teléfono 2"), max_length=20, blank=True, null=True)
    address = models.TextField(_("Dirección"))

    class Meta:
        verbose_name = _("technician")
        verbose_name_plural = _("technicians")

    def __str__(self):
        return f'ID:{self.pk} | {self.user.first_name} {self.user.last_name}'


class Plan(models.Model):
    plan = models.CharField(_("Plan"), max_length=50)

    class Meta:
        verbose_name = _("plan")
        verbose_name_plural = _("plans")

    def __str__(self):
        return self.plan


class CustomerType(models.Model):
    customer_type = models.CharField(_("Tipo de cliente"), max_length=50)

    class Meta:
        verbose_name = _("customertype")
        verbose_name_plural = _("customertypes")

    def __str__(self):
        return self.customer_type


class Municipality(models.Model):
    name = models.CharField(_("Nombre"), max_length=50)
    
    class Meta:
        verbose_name = _("municipality")
        verbose_name_plural = _("municipalities")

    def __str__(self):
        return self.name


class InstallationCategory(models.Model):
    installation_category = models.CharField(_("Categoría de instalación"), max_length=50)

    class Meta:
        verbose_name = _("installationcategory")
        verbose_name_plural = _("installationcategories")

    def __str__(self):
        return self.installation_category


class InstallationType(models.Model):
    installaion_type = models.CharField(_("Tipo de instalación"), max_length=50)

    class Meta:
        verbose_name = _("installationtype")
        verbose_name_plural = _("installationtypes")

    def __str__(self):
        return self.installaion_type


class DeviceList(models.Model):
    device_list = models.CharField(_("Equipos"), max_length=100)

    class Meta:
        verbose_name = _("devicelist")
        verbose_name_plural = _("devicelists")


    def __str__(self):
        return self.device_list

class Customer(models.Model):
    contract_number = models.IntegerField(_("Nro. De Contrato"), primary_key=True)
    name = models.CharField(_("Nombre Cliente"), max_length=100)

    email = models.EmailField(_("Email"), max_length=254, blank=True, null=True)
    phone_1 = models.CharField(_("Teléfono 1"), max_length=20)
    phone_2 = models.CharField(_("Teléfono 2"), max_length=20, blank=True, null=True)
    municipality = models.ForeignKey(Municipality, verbose_name=_("Municipio"), on_delete=models.SET_NULL, blank=True, null=True)
    address = models.TextField(_("Dirección"))

    longitude = models.FloatField(_("Longitud"), blank=True, null=True)
    latitude = models.FloatField(_("Latitud"), blank=True, null=True)

    plan = models.ForeignKey(Plan, verbose_name=_("Plan"), on_delete=models.CASCADE)
    customer_type = models.ForeignKey(CustomerType, verbose_name=_("Tipo de cliente"), on_delete=models.CASCADE)

    assigned_company = models.CharField(_("Compañía asignada"), max_length=100, blank=True, null=True)
    seller = models.CharField(_("Vendedor"), max_length=100, blank=True, null=True)

    comment = models.TextField(_("Observaciones"), blank=True, null=True)
    
    date_received = models.DateField(_("Fecha de recepción"), blank=True, null=True)

    installation_category = models.ForeignKey(InstallationCategory, verbose_name=_("Categoría"), on_delete=models.CASCADE)
    installation_type = models.ForeignKey(InstallationType, verbose_name=_("Tipo de instalación"), on_delete=models.CASCADE)
    device_list = models.ForeignKey(DeviceList, verbose_name=_("Equipos"), on_delete=models.CASCADE, blank=True, null=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("customer")
        verbose_name_plural = _("customers")

    def __str__(self):
        return f'{self.contract_number}: {self.name}'



class Device(models.Model):
    serial = models.CharField(_("Serial"), max_length=25, primary_key=True)
    technician = models.ForeignKey(Technician, verbose_name=_("Técnico"), on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'ID: {self.serial}'


class ONU(Device):

    class Meta:
        verbose_name = _("onu")
        verbose_name_plural = _("onus")


class Router(Device):

    class Meta:
        verbose_name = _("router")
        verbose_name_plural = _("routers")


class Mininode(Device):

    class Meta:
        verbose_name = _("mininode")
        verbose_name_plural = _("mininodes")


class DROP(models.Model):
    serial = models.IntegerField(_("Serial"))
    total_length = models.IntegerField(_("Metraje total"))

    class Meta:
        verbose_name = _("drop")
        verbose_name_plural = _("drops")

    def __str__(self):
        return f'DROP ID: {self.serial}'


class KardexDROP(models.Model):
    drop = models.ForeignKey(DROP, verbose_name=_("Drop"), on_delete=models.CASCADE)
    length = models.IntegerField(_("Metraje"))
    technician = models.ForeignKey(Technician, verbose_name=_("Técnico"), on_delete=models.CASCADE, blank=True, null=True)
    output = models.BooleanField(_("Salida"))

    class Meta:
        verbose_name = _("kardexdrop")
        verbose_name_plural = _("kardexdrops")

    def __str__(self):
        return f'DROP: {self.drop} | {"Salida" if self.output else "Entrada"}'


class KardexTensioners(models.Model):
    quantity = models.IntegerField(_("Cantidad"))
    technician = models.ForeignKey(Technician, verbose_name=_("Técnico"), on_delete=models.CASCADE, blank=True, null=True)
    output = models.BooleanField(_("Salida"))

    class Meta:
        verbose_name = _("kardextensioners")
        verbose_name_plural = _("kardextensioners")

    def __str__(self):
        return f'Cantidad: {self.quantity} | {"Salida" if self.output else "Entrada"}'


class DelayedReason(models.Model):
    delayed_reason = models.CharField(_("Motivo demora"), max_length=50)

    class Meta:
        verbose_name = _("delayedreason")
        verbose_name_plural = _("delayedreasons")

    def __str__(self):
        return f'{self.pk}: {self.delayed_reason}'



class Installation(models.Model):
    

    customer = models.OneToOneField(Customer, verbose_name=_("Cliente"), on_delete=models.CASCADE)
    technician = models.ForeignKey(Technician, verbose_name=_("Técnico"), on_delete=models.CASCADE, blank=True, null=True)
    
   
    onu = models.OneToOneField(ONU, verbose_name=_("ONU"), on_delete=models.SET_NULL, blank=True, null=True)
    router = models.OneToOneField(Router, verbose_name=_("Router"), on_delete=models.SET_NULL, blank=True, null=True)
    mininode = models.OneToOneField(Mininode, verbose_name=_("Mininodo"), on_delete=models.SET_NULL, blank=True, null=True)

    date = models.DateField(_("Fecha"), blank=True, null=True)
    time = models.TimeField(_("Hora"), blank=True, null=True)

    zone = models.IntegerField(_("Zona"), blank=True, null=True)
    olt = models.IntegerField(_("OLT"), blank=True, null=True)
    card = models.IntegerField(_("Tarjeta"), blank=True, null=True)
    pon = models.IntegerField(_("PON"), blank=True, null=True)
    box = models.IntegerField(_("Caja"), blank=True, null=True)
    port = models.IntegerField(_("Puerto"), blank=True, null=True)

    box_power = models.FloatField(_("Potencia caja"), blank=True, null=True)
    house_power = models.FloatField(_("Potencia casa"), blank=True, null=True)   

    drop = models.ForeignKey(DROP, verbose_name=_("Serial DROP"), on_delete=models.CASCADE, blank=True, null=True)
    drop_length = models.IntegerField(_("Metraje DROP"), blank=True, null=True)

    num_tensioners = models.IntegerField(_("Cantidad de tensores"), blank=True, null=True)
    num_connectors = models.IntegerField(_("Cantidad de conectores"), blank=True, null=True)

    customer_confirm = models.BooleanField(_("Confirmación del cliente"), blank=True, null=True)

    completed = models.BooleanField(_("Completada"))
    delayed = models.BooleanField(_("Demorada"))
    delayed_reason = models.ForeignKey(DelayedReason, verbose_name=_("Motivo demora"), on_delete=models.CASCADE, blank=True, null=True)
    other_reason = models.CharField(_("Otro"), max_length=100, blank=True, null=True)

    history = HistoricalRecords()

    class Meta:
        verbose_name = _("installation")
        verbose_name_plural = _("installations")

    def __str__(self):
        return f'{self.customer.contract_number}' 

