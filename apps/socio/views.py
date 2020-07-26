# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
#from django.contrib.auth import login, logout as django_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from tablib import Dataset

from django.http import HttpResponseRedirect

# from apps.socio.forms import FormularioLogin

from apps.socio.forms import SocioForm, PerfilForm #UsuarioForm
from apps.socio.models import Socio , CC_corriente, CC_asiento, Perfil
from apps.accounts.models import Account

from apps.socio.recursos_importar import SocioResource, ActualizarCcResource, ActualizarAsientoResource

from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm



# class Perfil_Socio(TemplateView):
#     template_name = 'socio/perfil_socio.html'
class Actualizado_ok(TemplateView):
    template_name = 'socio/importar/actualizado_ok.html'

class Actualizado_error(TemplateView):
    template_name = 'socio/importar/actualizado_error.html'


# from django.contrib.auth import get_user_model
# User = get_user_model()
 
# class model_form_upload(UpdateView):
#     form_class = PerfilForm
#     success_url = "socio/test_subir_img.html"
 
#     def get_object(self):
#         user = get_object_or_404(User, username__iexact=self.kwargs.get("email"))
#         return get_object_or_404(UserProfile,user=user)


# class Perfil_Actualizar(UpdateView):
#     model = Perfil
#     form_class = PerfilForm
#     template_name = 'socio/test_subir_img.html'
#     success_url = reverse_lazy('socio:perfil')



class Perfil_Actualizar(UpdateView):
    model = Socio
    second_model = Perfil
    template_name = 'socio/perfil_socio.html' #'socio/test_subir_img.html'
    form_class = SocioForm
    second_form_class = PerfilForm
    success_url = reverse_lazy('socio:actualizado_ok')
    #success_url="/socio/perfil/{model.id_perfil}/"
    #context_object_name = 'asientos'

    # def get_success_url(self, **kwargs):
    #   return reverse('socio:perfil', args=[str(self.kwargs.get('pk', 0))])


    def get_context_data(self, **kwargs):
        context = super(Perfil_Actualizar, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        #print("imprimo pk: " + str(pk))
        socio = self.model.objects.get(id_socio=pk)
        perfil = self.second_model.objects.get(id_perfil=socio.perfil_id)
        #print("imprimo id_perfil: " + str(pk) + " imprimo id_perfil desde socio :" + str(socio.perfil_id))
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=perfil)
        context['id'] = pk
        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        #id_socio = kwargs['pk']
        perfil_id = kwargs['pk']
        socio = self.model.objects.get(id_socio=perfil_id)
        perfil = self.second_model.objects.get(id_perfil=perfil_id)

        form = self.form_class(request.POST, instance=socio)
        form2 = self.second_form_class(request.POST, instance=perfil)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())

    # def get_context_data(self, **kwargs):
    #     context = super(AuthorCreate, self).get_context_data(**kwargs)
    #     if int(self.kwargs['user_id']) != self.request.user.id:
    #         raise PermissionDenied
    #     return context

    # def get_queryset(self):
    #     #filtro la cuenta corriente del usuario logueado
    #     return Socio.objects.filter(id_cc=self.request.user.id_cc)


class Cc_asiento(ListView):
    model = CC_asiento
    #template_name = 'socio/perfil_socio.html'
    template_name = 'socio/cc_asiento.html'
    context_object_name = 'asientos'
    #context_object_name = 'cc_socio'
    #queryset = Usuario.objects.filter(borrado_logico = False)
    #queryset = Socio.objects.filter(id_cc = '1')

    def get_queryset(self):
        #filtro la cuenta corriente del usuario logueado
        #print(self.request.user.id_socio)
        return CC_asiento.objects.filter(cuenta=self.request.user.id_socio).order_by('-id')




class Cc_socio(ListView):
	model = CC_corriente
	#template_name = 'socio/perfil_socio.html'
	template_name = 'socio/cc_socio.html'
	context_object_name = 'asientos'
    #context_object_name = 'cc_socio'
    #queryset = Usuario.objects.filter(borrado_logico = False)
	#queryset = Socio.objects.filter(id_cc = '1')

	def get_queryset(self):
		#filtro la cuenta corriente del usuario logueado
        #print(self.request.user.id_socio)
		return CC_corriente.objects.filter(id_cc=self.request.user.id_socio)




# class Login(FormView):
#     template_name = 'index.html'
#     form_class = FormularioLogin
#     #success_url = reverse_lazy('index')
#     #success_url = reverse_lazy('post-list')
#     success_url = reverse_lazy('socio:perfil')

#     @method_decorator(csrf_protect)
#     @method_decorator(never_cache)
#     def dispatch(self,request,*args,**kwargs):
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return super(Login,self).dispatch(request,*args,**kwargs)
#             #print('error')

#     def form_valid(self,form):
#         login(self.request,form.get_user())
#         return super(Login,self).form_valid(form)

# @login_required
# def logout(request):
#     django_logout(request)
#     return  HttpResponseRedirect('/')

# class ControlPanelView(LoginRequiredMixin, TemplateView):
#     template_name = 'socio/perfil.html'
#     def get_context_data(self, **kwargs):
#             context = super(ControlPanelView, self).get_context_data(**kwargs)
#             context['socios'] = Socio.objects.pendientes()
#             # ....
#             # Recopilar resto de la informacion
#             # ....

#             return context

#documentacion del metodo
# https://django-import-export.readthedocs.io/en/latest/import_workflow.html
def importar_Socios_Excel(request):
   #template = loader.get_template('export/importar.html')
   if request.method == 'POST':
     socio_resource = SocioResource()
     dataset = Dataset()
    #  print(dataset)
     nuevos_socios = request.FILES['xlsfile']
    #  print(nuevos_socios)
     imported_data = dataset.load(nuevos_socios.read())
    #  print(dataset)
     result = socio_resource.import_data(dataset, dry_run=False, raise_errors=True) 
    #  print(result.has_errors())
     #diff.compare_with(self, instance, dry_run)
     if not result.has_errors():
        socio_resource.import_data(dataset, dry_run=True) # Importar
             # Add imported objects to LogEntry
   return render(request, 'socio/importar_socio.html')

def actualizar_CC_Excel(request):
   #template = loader.get_template('export/importar.html')
   if request.method == 'POST':
     cc_resource = ActualizarCcResource()
     dataset = Dataset()
    #  print(dataset)
     cc_actualizar = request.FILES['xlsfile']
    #  print(cc_actualizar)
     imported_data = dataset.load(cc_actualizar.read())
    #  print(dataset)
     result = cc_resource.import_data(dataset, dry_run=False, raise_errors=True) 
    #  print(result.has_errors())
     #diff.compare_with(self, instance, dry_run)
     
     if not result.has_errors():
       
        cc_resource.import_data(dataset, dry_run=True) # Importar
             # Add imported objects to LogEntry
   return render(request, 'socio/importar/actualizar_cc.html')

#el de arriba actualiza cc y este asientos
def actualizar_asiento_CC_Excel(request):
		#template = loader.get_template('export/importar.html')
	if request.method == 'POST':
		try:
			cc_resource = ActualizarAsientoResource()
			dataset = Dataset()
			# print(dataset)
			#try:
			cc_actualizar = request.FILES['xlsfile']
			#except ValueError:
			# print('??????????????/')
			#print(cc_actualizar)
			imported_data = dataset.load(cc_actualizar.read())
			# print(dataset)
			
			result = cc_resource.import_data(dataset, dry_run=False, raise_errors=True) 
			# print(result.has_errors())
			# print(ValueError)
			#diff.compare_with(self, instance, dry_run)
			if not result.has_errors():
				cc_resource.import_data(dataset, dry_run=True) # Importar
				return redirect('socio:actualizado_ok')

			# else:
			# 	return redirect('socio:actualizado_error')
		except:
			# print('Verifique que los campos de archivo y que los datos por ejemplo ticket y cc existan en la base y vuelva a intentarlo')
			return redirect('socio:actualizado_error')

             # Add imported objects to LogEntry
	return render(request, 'socio/importar/asiento.html')





class ListarSocio(ListView):
    model = Socio
    template_name = 'socio/listar_socio.html'
    context_object_name = 'socio'
    paginate_by = 10
    #queryset = socio.objects.filter(borrado_logico = False)

class EditarSocio(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socio/crear_socop.html'
    success_url = reverse_lazy('socio:perfil')



# from django.contrib import messages
# from django.contrib.auth import update_session_auth_hash
# from django.contrib.auth.forms import PasswordChangeForm
# from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Su contraseña fue actualizada con éxito!')
            return redirect('change_password')
        else:
            messages.error(request, 'Por favor corrija el error a continuación.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'socio/change_password.html', {
        'form': form
    })



