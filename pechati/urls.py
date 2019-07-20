from django.conf.urls import url
from pechati.views import base_view, pricelist_view
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', base_view, name='base'),
    url(r'^contacts$', TemplateView.as_view(template_name='contacts.html'), name='contacts'),
    url(r'^pricelist$', pricelist_view, name='pricelist'),
    url(r'^oplata_dostavka$', TemplateView.as_view(template_name='oplata_dostavka.html'), name='oplata_dostavka'),

]
