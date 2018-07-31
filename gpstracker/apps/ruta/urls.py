from django.conf.urls import url
from django.contrib.auth.views import login_required

from apps.ruta.views import index_ruta, RutaList, RutaCreate, RutaUpdate, \
	RutaDelete

urlpatterns = [
    url(r'^index$', index_ruta),
    url(r'^ruta/listar$', login_required(RutaList.as_view()), name='ruta_listar'),
    url(r'^ruta/nueva$', login_required(RutaCreate.as_view()), name='ruta_crear'),
    url(r'^ruta/editar/(?P<pk>\d+)$', login_required(RutaUpdate.as_view()), name='ruta_editar'),
    url(r'^ruta/eliminar/(?P<pk>\d+)$', login_required(RutaDelete.as_view()), name='ruta_eliminar'),

]