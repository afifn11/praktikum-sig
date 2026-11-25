from django.urls import path
from django.views.generic import RedirectView

from . import view_peta

app_name = 'petaindonesia'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='petaindonesia:peta_dasar', permanent=False)),
    path('dasar/', view_peta.peta_dasar, name='peta_dasar'),
    path('provinsi/', view_peta.peta_provinsi, name='peta_provinsi'),
    path('petani_jawa/', view_peta.petani_jawa, name='petani_jawa'),
]
