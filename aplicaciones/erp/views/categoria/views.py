from django.shortcuts import render
from django.urls import reverse_lazy

from aplicaciones.erp.forms import CategoryForm
from aplicaciones.erp.models import Category

#vistas genericas de django
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
#decorador
from django.utils.decorators import method_decorator


#Vistas basadas en funcion
def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all(),
    }
    return render(request, 'categoria/listar.html', data)


#Lista basada en clases con vistas genericas de Django
#Trabajar con clases es mas eficientes
class CategoryListView(ListView):
    model = Category
    template_name = 'categoria/listar.html'

    #Metodo para mandar parametros a traves de vistas basadas en clase
    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Listado de Categorías'
        return contex


#Crear vista  basada en clases con vistas genericas de Django



class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categoria/registrar.html'
    #reverse_lazy para redireccionar a una plantilla
    success_url = reverse_lazy('erp:listarCategoria')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['title'] = 'Crear Categoría'
        return contex

