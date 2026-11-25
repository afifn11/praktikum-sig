from django.shortcuts import render


def peta_dasar(request):
    """Render basic Leaflet map with multiple basemaps and vector overlays."""
    return render(request, 'petaindonesia/peta_dasar.html')


def peta_provinsi(request):
    """Render Indonesian 34 provinces map with searchable sidebar."""
    return render(request, 'petaindonesia/peta_provinsi.html')


def petani_jawa(request):
    """Render Java Island agricultural & population density choropleth map."""
    return render(request, 'petaindonesia/petani_jawa.html')
