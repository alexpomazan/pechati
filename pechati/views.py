from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from pechati.models import Pechat, Osnastka, Klishe
from django.core.mail import send_mail

def base_view(request):
    pechati_objects = Pechat.objects.all()
    return render(request, 'base.html', {'pechati_objects': pechati_objects})


def pricelist_view(request):
    osnastki_list = Osnastka.objects.all()
    return render(request, 'pricelist.html', {'osnastki_list': osnastki_list})


def pechatip_view(request):
    pechatip_list = Klishe.objects.filter(form='ip')
    send_mail(
        'Evil',
        'Ne besi menya, kozel!!!',
        settings.EMAIL_HOST_USER,
        ['aleksey.pomazan@gmail.com'],
        fail_silently=True,
    )
    return render(request, 'pechatip.html', {'pechatip_list': pechatip_list})
