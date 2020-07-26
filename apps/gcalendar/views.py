from django.shortcuts import render
from django.views.generic import TemplateView

from apps.slider_manager.models import banner_socios_protectores


# Create your views here.

# class Congreso(TemplateView):
# 	#pass
#     template_name = 'gcalendar/congreso.html'

# class Dermatologico(TemplateView):
# 	#pass
#     template_name = 'gcalendar/dermatologico.html'


def eventos(request):

    queryset = banner_socios_protectores.objects.all()
    
    context = {
        'slider_data': queryset[0]
    }
    return render(request, 'gcalendar/congreso.html', context)