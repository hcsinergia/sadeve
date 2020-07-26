# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.urls import path
#from apps.usuario.views import EliminarUsuario, CrearUsuario, ListarSocio, importar_Clientes_Excel
from apps.socio.views import Cc_asiento, actualizar_asiento_CC_Excel, Actualizado_ok, Actualizado_error, Perfil_Actualizar, Socio, ListarSocio, importar_Socios_Excel, actualizar_CC_Excel, Cc_socio, EditarSocio

from django.contrib.auth import views as auth_views

urlpatterns = [
	#path('exportar_socio_excel/', login_required(Exportar_Clientes_Excel.as_view()), name='exportar_socio_excel'),
 	path('importar_socio_excel/',importar_Socios_Excel, name = 'importar_socio_excel'),
 	path('actualizarcc/',actualizar_CC_Excel, name = 'actualizarcc'),
 	
 	#modificar nombre de la clase
	# path('cuentaCorriente/',actualizar_CC_Excel, name = 'cuentaCorriente'),
	path('actualizar_asiento/',actualizar_asiento_CC_Excel, name = 'actualizar_asiento'),
	

	#path('crear_usuario/',login_required(CrearUsuario.as_view()), name = 'crear_usuario'),
	path('listar_socio/', ListarSocio, name = 'listar_socio'),
	path('editar_socio/<int:pk>/',login_required(EditarSocio.as_view()), name = 'editar_socio'),

	path('cc_asiento/',login_required(Cc_asiento.as_view()), name = 'cc_asiento'),
	path('actualizado_ok/',login_required(Actualizado_ok.as_view()), name = 'actualizado_ok'),
	path('actualizado_error/',login_required(Actualizado_error.as_view()), name = 'actualizado_error'),
	# path('cc_socio/',login_required(Cc_socio.as_view()), name = 'cc_socio'),
	path('perfil/<int:pk>/',login_required(Perfil_Actualizar.as_view()), name = 'perfil'),

	#path('password/', auth_views.PasswordChangeDoneView.as_view(), name='password'),
	#path('change_password/', auth_views.password, name='change_password'),

	# path('perfil_actualizar/<int:pk>/',Perfil_Actualizar.as_view(), name = 'perfil_actualizar'),

	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),







#USUARIOOOOO ver
#https://simpleisbetterthancomplex.com/series/2017/09/25/a-complete-beginners-guide-to-django-part-4.html#password-change-view

]