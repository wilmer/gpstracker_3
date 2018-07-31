from django import forms

from apps.cliente.models import Cliente


class ClienteForm(forms.ModelForm):

	class Meta:
		model = Cliente

		fields = [
			'nombre',
			'sexo',
			'edad_aproximada',
			'fecha_nacimiento',
			'persona',
			'ocupacion',
		]
		labels = {
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad aproximada',
			'fecha_rescate':'Fecha de rescate',
			'persona': 'Cliente',
			'ocupacion': 'Ocupacion',
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
			'ocupacion': forms.CheckboxSelectMultiple(),
		}