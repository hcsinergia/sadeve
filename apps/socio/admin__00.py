# -*- coding: utf-8 -*-

from django.contrib import admin

#para resolver el problema del password en el administrador 
#importo para crear una clase y extender de UserAdmin 
from django.contrib.auth.admin import UserAdmin 
#
from apps.socio.models import Socio, CC_corriente, Estado, Categoria, Especialidad, Perfil, Concepto
#


#creo una clase personalizada que extiende de UserAdmin
# class SocioUserAdmin(UserAdmin):
# 	fieldsets = ()
# 	add_fieldsets = (
# 		(None,{
# 			'fields':('email_1','password1','password2',)
# 		}),
# 	)
# 	list_display = ('email_1','is_active','is_staff',)
# 	search_fields = ('email_1')
# 	ordening = ('email_1',)
	

admin.site.register(Socio)
#admin.site.register(Socio)
# admin.site.register(CC_corriente)
# admin.site.register(Estado)
# admin.site.register(Categoria)
# admin.site.register(Especialidad)
# admin.site.register(Perfil)
# admin.site.register(Concepto)
