from django.shortcuts import render

from .models import About
from apps.slider_manager.models import banner_socios_protectores


def about(request):
    queryset = About.objects.all()
    queryset_banner = banner_socios_protectores.objects.all()


    context = {
        'about_data': queryset[0],
        'slider_data': queryset_banner[0]

    }

    return render(request, 'about-us.html', context)