# -*- coding: utf-8 -*-
from django.db import models
# from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
#from django.contrib.auth.models import UserManager
# from apps.account.models import Account
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# DELETE FROM tu_tabla;
# VACUUM;

class Categoria(models.Model):

    '''
        Clase pensada para separar los estados si son estados de informes (informado o no informado)
        o
        Estado de cliente (activo o no activo)
    '''

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    categoria = models.CharField(max_length=200, null=True, blank=True)
    codigo = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return '{}'.format(str(self.categoria))



class Especialidad(models.Model):

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    especialidad = models.CharField(max_length=200, null=False, blank=False)
    slug = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.especialidad)



class Estado(models.Model):

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"

    categoria = models.ForeignKey(Categoria, null=True, blank=True, on_delete=models.CASCADE)
    estado = models.CharField(max_length=200, null=False, blank=False)
    slug = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.estado)

class Concepto(models.Model):

    class Meta:
        verbose_name = "Concepto"
        verbose_name_plural = "Conceptos"

    concepto = models.CharField(max_length=200, null=False, blank=False)
    slug = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return '{}'.format(self.concepto)





class Perfil(models.Model):

	class Meta:
		verbose_name = "Perfil"
		verbose_name_plural = "Perfiles"

	id_perfil = models.AutoField(primary_key = True)
	matricula = models.CharField(unique=True, max_length=200, null=True, blank=True)
	email_2 = models.CharField(max_length=200, null=True, blank=True)
	tel_personal = models.IntegerField(null=True, blank=True)
	tel_laboral = models.IntegerField(null=True, blank=True)
	domicilio_fiscal = models.CharField(max_length=200, null=True, blank=True)
	domicilio_postal = models.CharField(max_length=200, null=True, blank=True)
	especialidad_principal = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True, blank=True)
	#otras_especialidades = models.ForeignKey(Especialidad, on_delete=models.CASCADE, null=True, blank=True)
	observacion = models.TextField(max_length=300, blank = True) 
	imagen = models.ImageField(upload_to = 'perfil_socio', default = '/media/perfil_socio/sin_imagen.jpg', blank=True, null=True) 

	def __str__(self):
	    return '{}'.format(str(self.id_perfil))

# class SocioManager(BaseUserManager):
	
# 	# def create_user(self, email_1, password=None, **kwargs):
# 	# 	user = self.model(usuario = email_1)
# 	# 	user.set_password(password)
# 	# 	user.save(using=self._db)
# 	# 	return user

# 	def create_user(self, email_1, nombre_1, apellido_1, password=None):
# 		"""
# 		Crea y guarda un usuario no administrador con el correo electrónico, fecha de
# 		nacimiento y contraseña
# 		"""
# 		if not email_1:
# 			raise ValueError('El usuario debe ser una direcion de email')

# 		user = self.model(
# 			email_1=self.normalize_email(email_1),
# 			nombre_1=nombre_1,
# 			apellido_1=apellido_1,
# 		)

# 		user.is_staff = False
# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user


# 	def create_superuser(self, email_1, nombre_1, apellido_1, password):
		
# 		user = self.create_user(
# 			email_1,
# 			password=password,
# 			nombre_1=nombre_1,
# 			apellido_1=apellido_1,
# 		)
# 		user.is_admin = True
# 		user.save(using=self._db)
# 		return user


# 	def get_cc(self):
# 		dato = self._cc_id
# 		print("aca llegue" + dato)
# 		return dato


#class Socio(models.Model):

class CC_corriente(models.Model):

	class Meta:
		verbose_name = "Cuenta Corriente"
		verbose_name_plural = "Cuenta Corriente"

	id_cc = models.AutoField(primary_key = True)
	cuenta_numero = models.IntegerField(null=True, blank=True)
	#id_cc = models.ForeignKey(Socio, on_delete=models.CASCADE, null=True, blank=True)
	cc_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
	fecha_publicado = models.DateTimeField(auto_now_add=True)
	#valor = models.FloatField(default='0.00')
	#concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=True, blank=True)
	#socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=False, blank=False)
	#content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		#return '{}'.format(str(self.id_cc))
		return '{} {}'.format(str(self.cuenta_numero),' - ' + str(self.socio.id_cc))
 


class Socio(Perfil, CC_corriente):

	class Meta:
		verbose_name = "Socio"
		verbose_name_plural = "Socios"

	#esta heredando de cc_corriente y de perfil

	id_socio = models.AutoField(primary_key = True)
	#user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	perfil = models.OneToOneField(Perfil, on_delete=models.CASCADE, null=True, blank=True)
	num_socio = models.CharField(unique=True, max_length=200, null=True, blank=True)
	dni = models.IntegerField(unique=True,null=True, blank=True)
	cuit = models.IntegerField(unique=True,null=True, blank=True)
	nombre_1 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Primer Nombre')
	nombre_2 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Segundo Nombre')
	apellido_1 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Primer Apellido')
	apellido_2 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Segundo Apellido')
	#email = models.CharField(unique=True, max_length=200, null=True, blank=True, verbose_name='direccion de email',)
	socio_estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=True, blank=True)
	#cc_corriente = models.OneToOneField(CC_corriente, on_delete=models.CASCADE, null=True, blank=True)
	#cuenta_corriente = models.ForeignKey(CC_corriente, on_delete=models.CASCADE, null=True, blank=True)
	fecha_alta = models.DateTimeField(auto_now_add=True)
	#is_admin = models.BooleanField(default=False)
	#is_active = models.BooleanField(default=True)
	#is_staff = models.BooleanField(default=False)
	borrado_logico = models.BooleanField('Borrado', default = False)


	# objects = SocioManager()

	# USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS = ['nombre_1', 'apellido_1']

	# # def __str__(self):
 # 	# 	return self.email

	# def get_full_name(self):
	# 	return self.email


	# def get_short_name(self):
	# 	return self.email

	# def has_perm(self, perm, obj=None):
	# 	"¿Tiene el usuario un permiso específico?"
	# 	# Respuesta más simple posible: Sí, siempre
	# 	return True

	# def has_module_perms(self, app_label):
	# 	"¿El usuario tiene permisos para ver la aplicación 'app_label'? "
	# 	# Respuesta más simple posible: Sí, siempre
	# 	return True

	# @property
	# def is_staff(self):
	# 	"¿Es el usuario un miembro del la asociacion?"
	# 	#La respuesta más simple posible: todos los administradores son personal de la asociacion
	# 	return self.is_admin
	
	def __str__(self):
		#return '{}{}{}'.format(str(self.id_socio) +" - "+str(self.nombre_1) +" - "+ str(self.apellido_1))
		return '{} {} {}'.format(str(self.id_socio),' - ' + str(self.nombre_1),' - ' + str(self.apellido_1))



class CC_asiento(models.Model):

	class Meta:	
		verbose_name = "Asiento"
		verbose_name_plural = "Asientos"

	ticket = models.IntegerField(unique=True,null=False, blank=False)
	#cuenta = models.ForeignKey(CC_corriente, on_delete=models.CASCADE, null=False, blank=False)
	# cuenta = models.IntegerField(unique=True,null=True, blank=True)
	cuenta = models.ForeignKey(CC_corriente, on_delete=models.CASCADE, null=False, blank=False)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE, null=False, blank=False)
	valor = models.FloatField(default='0.00')
	concepto = models.ForeignKey(Concepto, on_delete=models.CASCADE, null=False, blank=False)
	#socio = models.ForeignKey(Socio, on_delete=models.CASCADE, null=False, blank=False)
	fecha = models.DateTimeField(auto_now_add=True)
	#content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		#return '{}'.format(str(self.id_cc))
		return '{} {}'.format(str(self.concepto),' - ' + str(self.fecha),' - ' + str(self.valor),' - ' + str(self.estado))



