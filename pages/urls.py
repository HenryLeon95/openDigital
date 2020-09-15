from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categorias/', categoria, name='categorias'),
    path('productos/<id>', productos, name='productos'),
]