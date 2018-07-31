# -*- encoding:utf-8 -*-
from django import forms

from apps.ruta.models import Persona, Ruta



class PersonaForm(forms.ModelForm):

	class Meta:
		model = Persona
		fields = [
			'nombre',
			'apellidos',
			'edad',
			'telefono',
			'email',
			'domicilio',
		]
		labels = {
			'nombre': 'Nombre',
			'apellidos': 'Apellidos',
			'edad': 'Edad',
			'telefono': 'Teléfono',
			'email': 'Correo electrónico',
			'domicilio': 'Domicilio',
		}
		widgets = {
			'nombre':forms.TextInput(attrs={'class':'form-control'}),
			'apellidos':forms.TextInput(attrs={'class':'form-control'}),
			'edad':forms.TextInput(attrs={'class':'form-control'}),
			'telefono':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'domicilio':forms.Textarea(attrs={'class':'form-control'}),
		}


class RutaForm(forms.ModelForm):

	class Meta:
		model = Ruta
		fields = [
			'latitud', 
			'longitud', 
			'fecha_creacion',
			'altitud',
			'velocidad',
			'direccion_brujula',
			'precision',
			'proveedor',
		]
		labels = {
			'latitud':'Latitud', 
			'longitud':'Longitud', 
			'fecha_creacion':'Fecha Creación',
			'altitud':'Altitud',
			'velocidad':'Velocidad',
			'direccion_brujula':'Orientación',
			'precision':'Precisión',
			'proveedor':'Proveedor',
			
		}
		widgets = {
			'latitud':forms.TextInput(attrs={'class':'form-control'}),
			'longitud':forms.TextInput(attrs={'class':'form-control'}),
			'fecha_creacion':forms.TextInput(attrs={'class':'form-control'}),
			'altitud':forms.TextInput(attrs={'class':'form-control'}),
			'velocidad':forms.TextInput(attrs={'class':'form-control'}),
			'direccion_brujula':forms.TextInput(attrs={'class':'form-control'}),
			'precision':forms.TextInput(attrs={'class':'form-control'}),
			'proveedor':forms.TextInput(attrs={'class':'form-control'}),
			##'razones':forms.Textarea(attrs={'class':'form-control'}),
		}
