from django.shortcuts import render
from django.db.models import F
from django.views.generic import TemplateView, ListView, DetailView
from .models import Category, Product
import itertools

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

def categoria(request):
    categories_father = Category.objects.filter(father = 0).order_by('name')
    flag0 = True
    data={
        'categories':categories_father,
        'flag0': flag0
    }
    return render(request, 'Product/index.html',data)

def productos(request, id, opcion):
    flag0 = False #Para saber si hay sub categorias
    flag2 = False #Para saber si hay productos
    category_father = Category.objects.get(id = id)
    categories_father = Category.objects.filter(father = id).order_by('name')
    products = Product.objects.filter(category=id)
    name_category_father = category_father.name

    if categories_father.count() >= 1:
        name_category_father = name_category_father
        flag0 = True
    else:
        flag0 = False
        name_category_father = name_category_father

    if products.count() >= 1:
        flag2 = True
    else:
        flag2 = False


    if opcion == '0':
        products = products.order_by('item')
        print('Orden normal')
    elif opcion == '1':
        products = products.order_by(F('cost').asc())
        print('Orden ascendente')
    else:
        products = products.order_by(F('cost').desc())
        print('Orden descendente')

    data={
        'categories':categories_father,
        'products':products,
        'flag1': flag0,
        'name_category_father': name_category_father,
        'id': id,
        'flag2': flag2
    }
    print(id)
    return render(request, 'Product/index.html',data)