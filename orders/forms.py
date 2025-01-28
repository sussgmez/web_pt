from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import InstallationCategory, InstallationType, Customer, Installation



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'type':'text', 'class':'login-form-input', 'placeholder':'Nombre de usuario'}), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login-form-input', 'placeholder':'Contraseña'}), required=True)

    class Meta:
        model = User

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            self.fields['username'].widget.attrs['class'] = 'login-form-input error'
            self.fields['password'].widget.attrs['class'] = 'login-form-input error'

            raise forms.ValidationError("Correo o contraseña inválidos.")

        return self.cleaned_data
    
    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user



class CustomerCreateForm(forms.ModelForm):
    
    class Meta: 
        model = Customer
        fields = (
            "contract_number",
            "name", 
            "phone_1", 
            "phone_2", 
            "email", 
            "municipality", 
            "longitude", 
            "latitude", 
            "address", 

            "customer_type", 
            "installation_category",
            "installation_type",

            "plan", 
            "assigned_company", 
            "seller", 

            "date_received",
            "device_list",
            
            "comment", 
        )
        widgets = {
            'contract_number':forms.NumberInput(attrs={'class':'form-input', 'min':'1000000', 'max':'1099999', 'placeholder':' ', 'onkeyup':'check_contract_number(this.value)'}),
            'name':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'address':forms.Textarea(attrs={'rows':'2','class':'form-input','type':'textarea', 'placeholder':' '}),
            'longitude':forms.NumberInput(attrs={'class':'form-input', 'min':'1000000', 'max':'1099999', 'placeholder':' ', 'onkeyup':'check_contract_number(this.value)'}),
            'latitude':forms.NumberInput(attrs={'class':'form-input', 'min':'1000000', 'max':'1099999', 'placeholder':' ', 'onkeyup':'check_contract_number(this.value)'}),
            'phone_1':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'phone_2':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'email':forms.TextInput(attrs={'class':'form-input', 'placeholder':' ','type':'email'}),
            'plan':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'customer_type':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'installation_category':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'installation_type':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'device_list':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'municipality':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'category':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'assigned_company':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'seller':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'date_received':forms.DateTimeInput(format='%Y-%m-%d', attrs={'type':'date', 'class':'form-input', 'placeholder':' '}),
            'comment':forms.Textarea(attrs={'rows':'2','class':'form-input', 'placeholder':' '}),
        }

class CustomerUpdateForm(forms.ModelForm):
    
    class Meta: 
        model = Customer
        fields = (
            "name", 
            "phone_1", 
            "phone_2", 
            "email", 
            "municipality", 
            "longitude", 
            "latitude", 
            "address", 

            "customer_type", 
            "installation_category",
            "installation_type",

            "plan", 
            "assigned_company", 
            "seller", 

            "date_received",
            "device_list",
            
            "comment", 
        )
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'address':forms.Textarea(attrs={'rows':'2','class':'form-input','type':'textarea', 'placeholder':' '}),
            'longitude':forms.NumberInput(attrs={'class':'form-input', 'min':'1000000', 'max':'1099999', 'placeholder':' ', 'onkeyup':'check_contract_number(this.value)'}),
            'latitude':forms.NumberInput(attrs={'class':'form-input', 'min':'1000000', 'max':'1099999', 'placeholder':' ', 'onkeyup':'check_contract_number(this.value)'}),
            'phone_1':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'phone_2':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'email':forms.TextInput(attrs={'class':'form-input', 'placeholder':' ','type':'email'}),
            'plan':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'customer_type':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'installation_category':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'installation_type':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'device_list':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'municipality':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'category':forms.Select(attrs={'class':'form-input', 'placeholder':' '}),
            'assigned_company':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'seller':forms.TextInput(attrs={'class':'form-input', 'placeholder':' '}),
            'date_received':forms.DateTimeInput(format='%Y-%m-%d', attrs={'type':'date', 'class':'form-input', 'placeholder':' '}),
            'comment':forms.Textarea(attrs={'rows':'2','class':'form-input', 'placeholder':' '}),

        }

