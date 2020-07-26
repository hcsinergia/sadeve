# -*- coding: utf-8 -*-

from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from apps.socio.models import Socio, Perfil



class PerfilForm(forms.ModelForm):

    class Meta:
        model = Perfil
        fields = ['matricula','email_2','tel_personal','tel_laboral','domicilio_fiscal', 'domicilio_postal','observacion','especialidad_principal','imagen',] #,'otras_especialidades'
        labels = {
			'matricula':'matricula',
			'email_2':'email_2',
			'tel_personal':'tel_personal',
			'tel_laboral':'tel_laboral',
			'domicilio_fiscal':'domicilio_fiscal',
			'domicilio_postal':'domicilio_postal',
			'observacion':'observacion',
			'especialidad_principal':'especialidad_id',
			#'otras_especialidades':'otras_especialidades',
			'imagen':'imagen',

        }
        widgets = {
            'matricula': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'matricula',
                    'id': 'matricula'
                }
            ),

            'email_2': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'email secundario',
                    'id': 'email_2'
                }
            ),

            'tel_personal': forms.TextInput(
                attrs={
                    'required': True,
                    'class': 'form-control',
                    'placeholder': 'tel personal',
                    'id': 'tel_personal'
                }
            ),

            'tel_laboral': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'tel laboral',
                    'id': 'tel_laboral'
                }
            ),

            'domicilio_fiscal': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'domicilio fiscal',
                    'id': 'domicilio_fiscal'
                }
            ),

            'domicilio_postal': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'domicilio postal',
                    'id': 'domicilio_postal'
                }
            ),
            
            'especialidad_id':forms.Select(
                attrs = {
                    'class':'form-control',
                    'placeholder':'especialidad',
                    'id':'especialidad_id'
                }
            ),

            # 'otras_especialidades': forms.SelectMultiple(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'posee otras especialidade/s',
            #         'id': 'email_2'
            #     }
            # ),

            # 'imagen': forms.TextInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': '',
            #         'id': 'imagen'
            #     }
            # ),

            'observacion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'observaciones',
                    'id': 'observacion'
                }
            ),
        }


class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'



class SocioForm(forms.ModelForm):

    class Meta:
        model = Socio
        # fields = ['estudio','persona_tipo','cuit','condicion','razon_social', 'nombre_1','nombre_2','apellido_1','apellido_2','domicilio','email','email_2','telefono_1','telefono_2','estado',]
        fields = ['nombre_1','nombre_2', 'apellido_1','apellido_2','domicilio_postal','tel_laboral','tel_personal',] #,'email'
        labels = {
            'nombre_1':'Nombre',
            'apellido_1':'Apellido',
            #'email':'Email Principal',
            'tel_laboral': 'Tel. Principal',
            'tel_personal': 'Tel. Móvil',
            'domicilio':'Domicilio',

        }
        widgets = {
            'nombre_1': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese primer nombre',
                    'id': 'nombre_1'
                }
            ),
            
            'apellido_1': forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese primer apellido',
                    'id':'apellido_1'
                }
            ),
            

            # 'email': forms.EmailInput(
            #     attrs={
            #         'class': 'form-control',
            #         'placeholder': 'Ingrese email principal',
            #         'id': 'email'
            #     }
            # ),


            'tel_laboral': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese telefono laboral',
                    'id': 'telefono_laboral'
                }
            ),
            'tel_personal': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese telefono personal',
                    'id': 'telefono_personal'
                }
            ),

            'domicilio_postal':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese domicilio',
                    'id':'domicilio'
                }
            ),
        }

class Socio(forms.ModelForm):
	model = Socio
	class Meta:
		fields=['num_socio', 'dni', 'cuit', 'nombre_1', 'nombre_2', 'apellido_1', 'apellido_2', 'email', 'socio_estado'] #id, 
		labels = {
	            'num_socio':'num_socio',
	            'dni':'dni',
	            'cuit': 'cuit',
	            'nombre_1': 'nombre_1',
	            'nombre_2':'nombre_2',
	            'apellido_1':'apellido_1',
	            'apellido_2':'apellido_2',
	            'email':'Usuario',
	        }
		widgets = {
			'email': forms.TextInput(
				attrs= {
					'class': 'form-control',
					'placeholder': ' Nombre',
					'id': 'email',
					'readonly':'True',
					}

				),


		}


class UsuarioForm(forms.ModelForm):
    pass

    # class Meta:
    #     model = User
    #     #fields = ['dni','empleador','nombre_1','nombre_2','apellido_1','apellido_2','domicilio','email','email_2','telefono_1','telefono_2','estado',]
    #     #fields = ['dni_empleado','empleador_cuit','user','nombre_1','nombre_2','apellido_1','apellido_2','domicilio','email','email_2','telefono_1','telefono_2','estado',]
    #     fields = ['first_name','username','email', 'is_active']
    #     labels = {
    #
    #         'username':'Usuario',
    #         'first_name':'Nombre',
    #         'email': 'Email',
    #
    #     }
    #     widgets = {
    #         'first_name': forms.TextInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'placeholder': ' Nombre',
    #                 'id': 'first_name'
    #             }
    #         ),
    #
    #         'username': forms.TextInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'placeholder': ' Usuario',
    #                 'id': 'username'
    #             }
    #         ),
    #
    #         'email': forms.TextInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'placeholder': ' Email',
    #                 'id': 'email'
    #             }
    #         ),
    #
    #         # 'password': forms.PasswordInput(
    #         #     attrs={
    #         #         'class': 'form-control',
    #         #         'placeholder': 'Nuevo password',
    #         #         'id': 'password'
    #         #     }
    #         # ),
    #
    #
    #
    #
    #     }
