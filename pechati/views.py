from django.shortcuts import render
from pechati.models import Pechat, Osnastka


def base_view(request):
    pechati_objects = Pechat.objects.all()
    return render(request, 'base.html', {'pechati_objects': pechati_objects})


def pricelist_view(request):
    osnastki_list = Osnastka.objects.all()
    return render(request, 'pricelist.html', {'osnastki_list': osnastki_list})
