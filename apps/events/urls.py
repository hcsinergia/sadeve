# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.gcalendar.views import Congreso, Dermatologico
from apps.events.views import EventAdmin

urlpatterns = [
	
 	path('congreso/',EventAdmin.as_view(), name = 'congreso'),
 	path('dermatologico/',Dermatologico.as_view(), name = 'dermatologico'),
 	
]