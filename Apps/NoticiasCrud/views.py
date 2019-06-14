from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.NoticiasCrud.models import NoticiasModelo
from Apps.NoticiasCrud.forms import NoticiaCrearForm
# Create your views here.


def noticias_lista(request):
    datos = NoticiasModelo.objects.all()
    contexto = {'lista': datos}
    return render(request, 'noticias.html', contexto)


def noticias_crear(request):
    if request.method == "POST":
        form = NoticiaCrearForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('noticias_lista')
    else:
        form = NoticiaCrearForm()
    contexto = {'form': form}
    return render(request, 'noticias_crear.html', contexto)

def noticias_eliminar(request, id):
    # obtenemos el modelo taller
    noticia = NoticiasModelo.objects.get(id = id)
    if request.method == "POST":
        noticia.delete()
        return redirect('noticias_lista')
    else:
        return render(request, 'noticia_eliminar.html', {'noticia': noticia})

def noticias_editar(request, id):
    # otenemos el modelo taller
    noticia = NoticiasModelo.objects.get(id = id)
    if request.method == "GET":
        form=NoticiaCrearForm(instance=noticia)
    else:
        form=NoticiaCrearForm(request.POST, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticias_lista')
    contexto = {'form': form}
    return render(request, 'noticias_editar.html', contexto)