# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.urls import path

# from apps.gcalendar.views import Congreso, Dermatologico, 
from apps.gcalendar.views import eventos

urlpatterns = [
	
 	# path('congreso/',Congreso.as_view(), name = 'congreso'),

 	# path('congreso/',Congreso, name = 'congreso'),Eventos
	 path('eventos/',eventos, name = 'eventos'),
 	# path('dermatologico/',Dermatologico.as_view(), name = 'dermatologico'),

 	
]