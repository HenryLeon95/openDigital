from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Product

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def productos(request):
    categories_father = Category.objects.filter(father = 0)
    products = Product.objects.all()
    flag0 = False #Para saber si hay sub categorias
    data={
        'categories':categories_father,
        'products':products,
        'flag0': flag0
    }
    return render(request, 'Product/index.html',data)