from django import forms
from Apps.NoticiasCrud.models import *


class NoticiaCrearForm(forms.ModelForm):
    class Meta:
        model = NoticiasModelo

        fields = [
            'titulo',
            'resumen',
            'fecha',
            'detalle',
            'Familia',
        ]

        labels = {
            'titulo': 'Titulo',
            'resumen': 'Resumen',
            'fecha': 'Fecha',
            'detalle':'Detalle',
            'Familia': 'Familia',
        }

        widgets = {

            'titulo': forms.TextInput(attrs={'class': 'form-control'}),

            'resumen': forms.TextInput(attrs={'class': 'form-control'}),

            'fecha': forms.TextInput(attrs={'class': 'form-control'}),

            'detalle': forms.Textarea(attrs={'class': 'form-control'}),

            'Familia': forms.Select(attrs={'class': 'form-control'}),

        }
