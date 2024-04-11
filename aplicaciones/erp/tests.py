from SitioWeb.wsgi import *
from aplicaciones.erp.models import Type

#Listar

#Select * from tabla


#Lo que hace el ORM es que en lugar de usar
# una conculta como esta Select * from tabla  solo se manda a
# llamr el nombre del modelo con todos sus objetos


'''
#Listar
query = Type.objects.all()
for dato in query:
    print(dato)'''

#Insertar
'''
t = Type()
t.name = 'Presidente '
t.save()'''

'''
#Edicion
t = Type.objects.get(pk=3)
t.name = 'Director '
t.save()
'''

'''
#Eliminar
t = Type.objects.get(pk=4)
t.delete()

'''


#Listar con filtro
#Con icontains me muestra datos con mayuscula y minuscula
#con filter me muestra los datos que tengan esas cadenas que se mandadn
print("----------------- TIENEN LA LETRA A-----------------------")
t = Type.objects.filter(name__icontains='a')
for dato in t:
    print(dato)

print("----------------- TERMINAN CON A-----------------------")
#Los datos que empiezan con
t = Type.objects.filter(name__endswith='a')
for dato in t:
    print(dato)

print("---------------- CONTAR  ------------------------")
t = Type.objects.all().count()
print(t)





