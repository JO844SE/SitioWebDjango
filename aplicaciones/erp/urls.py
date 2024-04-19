from django.contrib import admin
from django.urls import path, include
from aplicaciones.erp import views
from aplicaciones.erp.views.categoria.views import *
from aplicaciones.erp.views.dashboard.views import *
from aplicaciones.erp.views.cliente.views import *
from aplicaciones.erp.views.producto.views import ProductListView,ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'erp'

urlpatterns = [
    path('categoria/list/', CategoryListView.as_view(), name='listarCategoria'),
    path('categoria/add/', CategoryCreateView.as_view(), name='crearCategoria'),
    path('categoria/edit/<int:pk>/', CategoyUpdateView.as_view(), name='editarCategoria'),
    path('categoria/delete/<int:pk>/', CategoyDeleteView.as_view(), name='eliminarCategoria'),
    #Producto
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    #Cliente
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/add/', ClientCreateView.as_view(), name='client_create'),
    path('client/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),
    #Dashboard
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    # path('producto/', views.Productos, name='products'),
]
