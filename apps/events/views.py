# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView


# Create your views here.
# 
class Congreso(TemplateView):
    #template_name = 'events/change_list.html'

class Dermatologico(TemplateView):
	pass
    # template_name = 'gcalendar/dermatologico.html'


