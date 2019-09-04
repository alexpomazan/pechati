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
    if request.method == 'POST':
        nameip = request.POST['name']
        quantity = request.POST['quant']
        message = 'Client: ' + nameip + ' Quantity:' + quantity
        send_mail(
            'Hi, man',
            message,
            settings.EMAIL_HOST_USER,
            ['eee4ew@netmail3.net'],
            fail_silently=True,
        )
    return render(request, 'pechatip.html', {'pechatip_list': pechatip_list})
