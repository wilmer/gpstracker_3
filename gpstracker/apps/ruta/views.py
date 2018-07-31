from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.ruta.models import Persona, Ruta
from apps.ruta.forms import PersonaForm, RutaForm


def index_ruta(request):
	return HttpResponse("soy la pagina principal de la app gpstracker")


class RutaList(ListView):
	model = Ruta
	template_name = 'ruta/ruta_list.html'


class RutaCreate(CreateView):
	model = Ruta
	template_name = 'ruta/ruta_form.html'
	form_class = RutaForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('ruta:ruta_listar')

	def get_context_data(self, **kwargs):
		context = super(RutaCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			ruta = form.save(commit=False)
			ruta.persona = form2.save()
			ruta.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))



class RutaUpdate(UpdateView):
	model = Ruta
	second_model = Persona
	template_name = 'ruta/ruta_form.html'
	form_class = RutaForm
	second_form_class = PersonaForm
	success_url = reverse_lazy('ruta:ruta_listar')


	def get_context_data(self, **kwargs):
	    context = super(RutaUpdate, self).get_context_data(**kwargs)
	    pk = self.kwargs.get('pk', 0)
	    ruta = self.model.objects.get(id=pk)
	    persona = self.second_model.objects.get(id=ruta.persona_id)
	    if 'form' not in context:
	    	context['form'] = self.form_class()
	    if 'form2' not in context:
	    	context['form2'] = self.second_form_class(instance=persona)
	    context['id'] = pk
	    return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_ruta = kwargs['pk']
		ruta = self.model.objects.get(id=id_ruta)
		persona = self.second_model.objects.get(id=ruta.persona_id)
		form = self.form_class(request.POST, instance=ruta)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())


class RutaDelete(DeleteView):
	model = Ruta
	template_name = 'ruta/ruta_delete.html'
	success_url = reverse_lazy('ruta:ruta_listar')