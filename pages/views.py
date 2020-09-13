from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Product
import itertools

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def productos(request):
    categories_father = Category.objects.filter(father = 0).order_by('name')
    products = Product.objects.all()
    iterator = itertools.count()
    flag0 = False #Para saber si hay sub categorias
    data={
        'categories':categories_father,
        'products':products,
        'flag0': flag0,
        'iterator': iterator
    }
    return render(request, 'Product/index.html',data)