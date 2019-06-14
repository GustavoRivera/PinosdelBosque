from django.urls import path, include
from Apps.Vista.views import *

# importamos de la app ventas
urlpatterns = [
       path('', index, name='index'),
       path('noticias/', noticias, name='noticias'),
       path('eventos/', eventos, name='eventos'),
       path('ver/<int:id>/', ver, name='ver'),
        
]