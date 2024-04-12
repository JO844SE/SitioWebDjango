from django.contrib import admin
from django.urls import path, include
from aplicaciones.erp import views
from aplicaciones.erp.views.categoria.views import *

app_name = 'erp'

urlpatterns = [
    path('', CategoryListView.as_view(), name='listarCategoria'),
    path('categoria/add/', CategoryCreateView.as_view(), name='crearCategoria'),
    # path('producto/', views.Productos, name='products'),
]
