from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Product
import itertools

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def categoria(request):
    categories_father = Category.objects.filter(father = 0).order_by('name')
    data={
        'categories':categories_father
    }
    return render(request, 'Product/index.html',data)

def productos(request, id):
    categories_father = Category.objects.filter(father = 0).order_by('name')
    products = Product.objects.all()
    category_father = "All"
    flag0 = False #Para saber si hay sub categorias
    data={
        'categories':categories_father,
        'products':products,
        'flag0': flag0,
        'iterator': category_father
    }
    print(id)
    return render(request, 'Product/index.html',data)