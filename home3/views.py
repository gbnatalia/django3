import datetime
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Client, Product, Order


def client(request):
    template_name = "home3\\list_items.html"
    clients = Client.objects.all()
    context = dict()
    context['title'] = "Клиенты"
    context['items'] = clients
    return render(request, template_name, context)


def product(request):
    template_name = "home3\\list_items.html"
    products = Product.objects.all()
    context = dict()
    context['title'] = "Товары"
    context['items'] = products
    return render(request, template_name, context)


def order(request):
    template_name = "home3\\list_items.html"
    orders = Order.objects.all()
    context = dict()
    context['title'] = "Заказы"
    context['items'] = orders
    return render(request, template_name, context)


class OrderProductView(TemplateView):
    template_name = 'home3\\order_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(OrderProductView, self).get_context_data(**kwargs)
        client = Client.objects.get(id=self.kwargs['pk'])
        orders = Order.objects.filter(client=client).all()
        context['client'] = client
        context['orders'] = orders
        context['title'] = "Список заказов клиента"
        return context


class ListClientProducts(TemplateView):
    template_name = 'home3\\products_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ListClientProducts, self).get_context_data(**kwargs)
        enddate = datetime.date.today()
        startdate = enddate - datetime.timedelta(days=self.kwargs['days'])
        client = Client.objects.get(id=self.kwargs['pk'])
        orders = Order.objects.filter(client=client).filter(order_date__range=[startdate, enddate]).all().order_by('order_date')
        context['client'] = client
        context['orders'] = orders
        context['title'] = "Список заказов клиента"
        return context
