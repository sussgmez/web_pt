from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from order_control.views import OrderListView, CustomerCreateView, load_excel, CustomerUpdateView, CustomerListView, OrderUpdateView, InstallationCreateView, create_order, delete_order, delete_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', RedirectView.as_view(url='orders/')),
    path('orders/', login_required(OrderListView.as_view()), name='order-list'),
    path('orders/<int:pk>', login_required(OrderUpdateView.as_view()), name='order-update'),
    path('orders/complete', login_required(InstallationCreateView.as_view()), name='order-complete'),
    path('customers/', login_required(CustomerListView.as_view()), name='customer-list'),
    path('customers/add', login_required(CustomerCreateView.as_view()), name='customer-create'),
    path('customers/<int:pk>', login_required(CustomerUpdateView.as_view()), name='customer-update'),
    path('load_excel/', load_excel, name='load-excel'),
    path('create_order/<int:pk>', create_order, name='create-order'),
    path('delete_order/<int:pk>', delete_order, name='delete-order'),
    path('delete_customer/<int:pk>', delete_customer, name='delete-customer'),
]
