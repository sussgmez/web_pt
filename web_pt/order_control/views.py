import pandas, math
from datetime import datetime
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CustomerForm, CustomerUpdatedForm, OrderUpdateForm, ShowCustomerAsForm, InstallationForm
from .models import Order, Technician, Customer, Installation


def check_nan(value):
    if type(value)==float and math.isnan(value):return ""
    return value


class CustomerListView(ListView):
    model = Customer
    template_name = "order_control/customer_list.html.html"
    paginate_by = 18
    ordering = 'contract_number'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["technicians"] = Technician.objects.all()
        return context

    def get_queryset(self):
        s_text = ""
        try: s_text = self.request.GET['search-text']
        except: pass

        sort_by = "-pk"
        try: sort_by = self.request.GET['sort-by']
        except: pass

        customers = Customer.objects.filter(pk__contains=s_text) | Customer.objects.filter(address__contains=s_text) | Customer.objects.filter(customer_name__contains=s_text)
        
        return customers.order_by(sort_by)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['s_text'] = self.request.GET['text']
            
            s_status = self.request.GET['status']
            sort_by = self.request.GET['sort_by']

            context['s_status'] = s_status
            context['sort_by'] = sort_by

            if s_status == 'all': context['all'] = 'selected'
            elif s_status == 'pend': context['pend'] = 'selected'
            elif s_status == 'assg': context['assg'] = 'selected'
            elif s_status == 'comp': context['comp'] = 'selected'

            if sort_by == 'pk': context['pk'] = 'selected'
            elif sort_by == 'date_assigned': context['date_assigned'] = 'selected'

        except: pass
        return context


class OrderUpdateView(UpdateView):
    model = Order
    template_name = "order_control/order.html"
    form_class = OrderUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["customer_form"] = ShowCustomerAsForm(instance=context['object'].customer)
        
        status = "Sin asignar"
        obj = context['object']
        if obj.completed: status = 'Finalizada'
        elif obj.closed: status = 'Cerrada, sin completar'
        elif obj.technician != None: status = 'Asignada'

        context['status'] = status
  
        return context

    def get_success_url(self):
        return reverse('order-update', kwargs={'pk':self.object.pk})


class OrderListView(ListView):
    model = Order
    template_name = "order_control/order_list.html"
    paginate_by = 12
    
    def get_queryset(self):
        s_text = ""
        try: s_text = self.request.GET['search-text']
        except: pass

        status = ""
        try: status = self.request.GET['status']
        except: pass

        sort_by = "-pk"
        try: sort_by = self.request.GET['sort-by']
        except: pass

        min_date = ""
        try: 
            min_date = self.request.GET['min-date']
        except: pass
        
        max_date = ""
        try: 
            max_date = self.request.GET['max-date']
        except: pass

        orders = Order.objects.filter(pk__contains=s_text) | Order.objects.filter(customer__pk__contains=s_text) | Order.objects.filter(customer__address__contains=s_text) | Order.objects.filter(customer__customer_name__contains=s_text)

        if min_date != "" and max_date != "":
            orders = orders.filter(date_assigned__range=[min_date, max_date])

        if status == 'to_assign':
            orders = orders.filter(technician__isnull=True).filter(completed=False)
        elif status == 'assigned':
            orders = orders.filter(technician__isnull=False).filter(completed=False)
        elif status == 'completed':
            orders = orders.filter(completed=True)
        elif status == 'closed':
            orders = orders.filter(closed=True).filter(completed=False)
        
        return orders.order_by(sort_by)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try: 
            context["search_text"] = self.request.GET['search-text']
        except: pass

        try: 
            status = self.request.GET['status']
            context["status"] = status
            if status == 'null': context['status_opt_1'] = 'selected'
            elif status == 'to_assign': context['status_opt_2'] = 'selected'
            elif status == 'assigned': context['status_opt_3'] = 'selected'
            elif status == 'completed': context['status_opt_4'] = 'selected'
            elif status == 'closed': context['status_opt_5'] = 'selected'
        except: pass

        context["sort_by"] = '-pk'
        try: 
            sort_by = self.request.GET['sort-by']
            context["sort_by"] = sort_by
            if sort_by == '-pk': context['sort_opt_1'] = 'selected'
            elif sort_by == 'customer': context['sort_opt_2'] = 'selected'
            elif sort_by == 'date_created': context['sort_opt_3'] = 'selected'
            elif sort_by == 'customer_address': context['sort_opt_3'] = 'selected'
        except: pass

        try: 
            context["min_date"] = self.request.GET['min-date']
        except: pass
        try: 
            context["max_date"] = self.request.GET['max-date']
        except: pass

        return context
    

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = "order_control/customer.html"
    form_class = CustomerUpdatedForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assigned_orders"] = Order.objects.filter(customer=self.object.contract_number).order_by('-pk')
        return context
    

    def get_success_url(self):
        return reverse('customer-list')


class CustomerCreateView(CreateView):
    model = Customer
    template_name = "order_control/customer_create.html"
    form_class = CustomerForm
    
    def get_success_url(self):
        return reverse('customer-list')
    

class InstallationCreateView(CreateView):
    model = Installation
    template_name = "order_control/complete_order_installation.html"
    form_class = InstallationForm  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order = Order.objects.get(id=self.request.GET['order']) 
        context['order'] = order
        context["customer_form"] = ShowCustomerAsForm(instance=order.customer)
        return context

    def form_valid(self, form):
        order = Order.objects.get(id=self.request.POST['order'])
        order.completed = True
        order.closed = True
        order.save()
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('order-update', kwargs={'pk': self.object.order.pk})

   
def load_excel(request):
    if request.POST:
        df = pandas.read_excel(request.FILES['excel_file'])
        file_name = request.FILES['excel_file'].name
        received_date_txt = ""
        received_date = datetime.now()
        for char in file_name: 
            if char.isnumeric(): received_date_txt+=char
        try:
            received_date = datetime(day=int(received_date_txt[0:2]), month=int(received_date_txt[2:4]), year=int(received_date_txt[4:8]))
        except: pass

        for id, values in df.iterrows():
            obj = ""
            created = False
            try:
                for i in range(0,12): values.iloc[i]
                obj, created = Customer.objects.get_or_create(contract_number=values.iloc[0])
            except Exception as e: print(e)
            if created:
                obj.customer_name = values.iloc[1].title()
                obj.phone_1 = values.iloc[5]
                obj.phone_2 = check_nan(values.iloc[6])
                obj.address = values.iloc[7].title()
                obj.email = check_nan(values.iloc[8])
                obj.assigned_to = check_nan(values.iloc[10]).title()
                obj.date_assigned = received_date
                
                category = "INS"
                seller = check_nan(values.iloc[3]).title()
                comment = check_nan(values.iloc[11]).capitalize()

                if "Migracion" in seller or "Migración" in seller or "Migracion" in comment or "Migración" in comment:
                    category = "MIG"
                    seller = ""

                if "MUDANZA" in values.iloc[3].upper():
                    category = "MUD"
                    seller = ""

                obj.comment = comment
                obj.seller = seller
                obj.category = category         

                plan = values.iloc[9].upper()
                cod_plan = 'BR'

                if "BASICO PLUS" in plan:
                    cod_plan = 'BP'
                elif "BASICO" in plan:
                    cod_plan = 'BA'
                elif "BRONCE" in plan:
                    cod_plan = 'BR'
                elif "PLATA" in plan:
                    cod_plan = 'PL'
                elif "ORO" in plan:
                    cod_plan = 'OR'
                elif "EMPRENDEDOR" in plan:
                    cod_plan = 'EM'
                elif "PRODUCTIVO PRO" in plan:
                    cod_plan = 'PP'
                elif "PRODUCTIVO" in plan:
                    cod_plan = 'PR'
                elif "VISIONARIO PRO" in plan:
                    cod_plan = 'VP'

                obj.plan = cod_plan

                obj.save()

    return redirect('customer-list')


def create_order(request, pk):
    order = Order.objects.create(customer=Customer.objects.get(pk=pk))
    return redirect('order-update', pk=order.pk)


def delete_order(request, pk):
    Order.objects.get(pk=pk).delete()
    return redirect('order-list')


def delete_customer(request, pk):
    Customer.objects.get(pk=pk).delete()
    return redirect('customer-list')