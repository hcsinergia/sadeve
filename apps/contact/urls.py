# -*- coding: utf-8 -*-

# from django.contrib.auth.decorators import login_required
from django.urls import path
from apps.contact import views
#from apps.usuario.views import EliminarUsuario, CrearUsuario, ListarSocio, importar_Clientes_Excel
# from apps.socio.views import Cc_asiento, actualizar_asiento_CC_Excel, Actualizado_ok, Actualizado_error, Perfil_Actualizar, Socio, ListarSocio, importar_Socios_Excel, actualizar_CC_Excel, Cc_socio, EditarSocio

# from django.contrib.auth import views as auth_views

urlpatterns = [
	#path('exportar_socio_excel/', login_required(Exportar_Clientes_Excel.as_view()), name='exportar_socio_excel'),
 	# path('importar_socio_excel/',importar_Socios_Excel, name = 'importar_socio_excel'),
 	# path('actualizarcc/',actualizar_CC_Excel, name = 'actualizarcc'),
	path('', views.contact, name='contact'),
]
 	
 	


