# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.NoticiasCrud.models import NoticiasModelo
from Apps.NoticiasCrud.forms import NoticiaCrearForm

# Create your views here.

def index(request):
    return render(request, 'home.html')

def noticias(request):
    datos = NoticiasModelo.objects.filter(Familia='N')
    contexto = {'lista': datos}
    return render(request, 'vistanoticias.html',contexto)

def eventos(request):
    datos = NoticiasModelo.objects.filter(Familia='E')
    contexto = {'lista': datos}
    return render(request, 'vistaeventos.html',contexto)


def ver(request, id):
    item = NoticiasModelo.objects.get(id = id)
    return render(request, 'ver.html', {'item': item})
