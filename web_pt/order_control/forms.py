from django import forms
from .models import Customer, Order, Installation


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['contract_number', 'category', 'customer_name', 'address', 'phone_1', 'phone_2', 'email', 'plan', 'customer_type', 'date_assigned', 'assigned_to', 'seller', 'comment']
        widgets = {
            "customer_name": forms.TextInput(attrs={'class':'col-all'}),
            "address": forms.Textarea(attrs={'class':'col-all', 'rows':'2'}),
            "comment": forms.Textarea(attrs={'class':'col-all', 'rows':'2'})
        }


class CustomerUpdatedForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['contract_number', 'category', 'customer_name', 'address', 'phone_1', 'phone_2', 'email', 'plan', 'customer_type', 'date_assigned', 'assigned_to', 'seller', 'comment']
        widgets = {
            "contract_number": forms.TextInput(attrs={'readonly':True}),
            "customer_name": forms.TextInput(attrs={'class':'col-all'}),
            "address": forms.Textarea(attrs={'class':'col-all', 'rows':'2'}),
            "comment": forms.Textarea(attrs={'class':'col-all', 'rows':'2'}),
            "date_assigned": forms.DateInput(format='%Y-%m-%d', attrs={'type':'date'}),
        }


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['technician', 'date_assigned', 'extra_order_comment']
        widgets = {
            'date_assigned':forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type':'datetime-local'}),
            'closed': forms.HiddenInput(),
            'extra_order_comment': forms.Textarea(attrs={'rows':'2'})
        }


class ShowCustomerAsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['contract_number', 'customer_name', 'plan', 'address', 'phone_1', 'phone_2', 'category', 'customer_type', 'comment']
        widgets = {
            "contract_number": forms.TextInput(attrs={'disabled':True}),
            "customer_name": forms.TextInput(attrs={'disabled':True}),
            "address": forms.Textarea(attrs={'disabled':True}),
            "plan": forms.Select(attrs={'disabled':True}),
            "phone_1": forms.TextInput(attrs={'disabled':True}),
            "phone_2": forms.TextInput(attrs={'disabled':True}),
            "email": forms.TextInput(attrs={'disabled':True}),
            "category": forms.Select(attrs={'disabled':True}),
            "customer_type": forms.Select(attrs={'disabled':True}),
            "comment": forms.Textarea(attrs={'disabled':True}),
        }


class InstallationForm(forms.ModelForm):
    class Meta:
        model = Installation
        fields = ["order", "zone", "olt", "pon", "card", "box", "port", "box_power", "house_power", "onu_serial", "router_serial", "drop_serial", "drop_used", "hook_used", "fast_conn_used", "extra_comment"]
        widgets = {
            'order': forms.HiddenInput()
        }