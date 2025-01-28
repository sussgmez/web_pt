from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from .models import Customer
from .forms import LoginForm, CustomerCreateForm, CustomerUpdateForm


class LoginView(View):
    template_name = "orders/login.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('customer-page')

        form = self.form_class
        return render(request, self.template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.login()
            if user is not None:
                login(request, user)
                return redirect('customer-page')
            else:
                return render(request, self.template_name,{'form':form})
        else:
            return render(request, self.template_name,{'form':form})
        

class CustomerPageView(TemplateView):
    template_name = "orders/customer_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["status_list"] = InstallationStatus.objects.all()
        return context
    

class CustomerListView(ListView):
    model = Customer
    template_name = "orders/customer_list.html"
    paginate_by = 12
    

class CustomerCreateView(CreateView):
    model = Customer
    template_name = "orders/customer_create.html"
    form_class = CustomerCreateForm

    def get_success_url(self): 
        return reverse('home')


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "orders/customer_update.html"
    form_class = CustomerUpdateForm


def logout_handler(request):
    logout(request)
    return redirect('login')