from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from apps.cliente.views import listadousuarios, index, cliente_view, cliente_list, cliente_edit, cliente_delete, \
	ClienteList, ClienteCreate, ClienteUpdate, ClienteDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', login_required(ClienteCreate.as_view()), name='cliente_crear'),
    url(r'^listar', login_required(ClienteList.as_view()), name='cliente_listar'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(ClienteUpdate.as_view()), name='cliente_editar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(ClienteDelete.as_view()), name='cliente_eliminar'),
    url(r'^listado', listadousuarios, name="listado"),
]
