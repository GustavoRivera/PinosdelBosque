from django.urls import path, include
from Apps.NoticiasCrud.views import *

# importamos de la app ventas
urlpatterns = [
        path('', noticias_lista, name='noticias_lista'),
        path('eliminar/<int:id>/', noticias_eliminar, name='noticias_eliminar'),
        path('editar/<int:id>/', noticias_editar, name='noticias_editar'),
        path('crear/', noticias_crear, name='noticias_crear'),

]
