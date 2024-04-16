from django.contrib import admin
from django.urls import path, include
from aplicaciones.erp import views
from aplicaciones.erp.views.categoria.views import *

app_name = 'erp'

urlpatterns = [
    path('categoria/list/', CategoryListView.as_view(), name='listarCategoria'),
    path('categoria/add/', CategoryCreateView.as_view(), name='crearCategoria'),
    path('categoria/edit/<int:pk>/', CategoyUpdateView.as_view(), name='editarCategoria'),
    path('categoria/delete/<int:pk>/', CategoyDeleteView.as_view(), name='eliminarCategoria'),
    # path('producto/', views.Productos, name='products'),
]
