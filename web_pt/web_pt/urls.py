from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from order_control.views import CustomerListView, CustomerCreateView, CustomerUpdateView, delete_customer, OrderListView, OrderUpdateView, create_order, delete_order, InstallationCreateView, TechnicianListView, load_excel, InstallationUpdateView

urlpatterns = [
    path('', RedirectView.as_view(url='orders/')),
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),
    path('customers/', login_required(CustomerListView.as_view()), name='customer-list'),
    path('customers/add', login_required(CustomerCreateView.as_view()), name='customer-create'),
    path('customers/<int:pk>', login_required(CustomerUpdateView.as_view()), name='customer-update'),
    path('customers/delete/<int:pk>', delete_customer, name='delete-customer'),
    path('orders/', login_required(OrderListView.as_view()), name='order-list'),
    path('orders/add/<int:pk>', create_order, name='create-order'),
    path('orders/<int:pk>', login_required(OrderUpdateView.as_view()), name='order-update'),
    path('orders/complete', login_required(InstallationCreateView.as_view()), name='order-complete'),
    path('orders/delete/<int:pk>', login_required(delete_order), name='delete-order'),
    path('installation/<int:pk>', login_required(InstallationUpdateView.as_view()), name='installation-update'),
    path('technicians/', login_required(TechnicianListView.as_view()), name='technician-list'),
    path('load_excel/', login_required(load_excel), name='load-excel'),
]
