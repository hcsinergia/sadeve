# -*- coding: utf-8 -*-

from import_export import resources
from apps.socio.models import Socio, CC_corriente, CC_asiento 

#from django.urls import reverse_lazy

class SocioResource(resources.ModelResource):
	class Meta:
		model = Socio
		import_id_fields = ('dni',)
		#exclude = ('id',)
		fields = ('nombre_1','nombre_2','apellido_1','apellido_2','num_socio','dni','cuit', 'cuenta_corriente_id', 'email_1', 'socio_estado', 'is_staff')
		#fields = ('id','num_socio', 'apellido', 'condicion', 'estudio', 'persona_tipo','estado', 'email_1', 'telefono_1')

# sqlite> DELETE FROM nombre_tabla;
# sqlite> VACUUM;

class ActualizarCcResource(resources.ModelResource):
	class Meta:
		model = CC_corriente
		import_id_fields = ('socio',)
		fields = ('id','cuenta_numero','socio','cc_estado','valor','concepto')

class ActualizarAsientoResource(resources.ModelResource):
	class Meta:
		model = CC_asiento
		import_id_fields = ('ticket',)
		fields = ('ticket','cuenta','estado','valor','concepto')
		#success_url = reverse_lazy('socio:actualizado_ok')


#IMPORTANTE
# El siguiente error se da porque el valor en el excel es incorrecto 
# Exception Value: CC_corriente matching query does not exist.

#ejemplo si el numero de cuenta = 100 y en la app no existe el numero 100 va a dar el error 
#ejemplo1 si el estado = 1 y no existe el esta 1 nos da el siguiente error
#Exception Value: Estado matching query does not exist.