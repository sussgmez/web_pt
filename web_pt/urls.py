from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from orders.views import LoginView, CustomerPageView, CustomerListView, CustomerCreateView, CustomerUpdateView, logout_handler

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='home')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_handler, name='logout'),
    path('home/', login_required(CustomerPageView.as_view()), name='customer-page'),
    path('customer/list/', login_required(CustomerListView.as_view()), name='customer-list'),
    path('customer/create/', login_required(CustomerCreateView.as_view()), name='customer-create'),
    path('customer/update/<int:pk>', login_required(CustomerUpdateView.as_view()), name='customer-update'),
    
]
