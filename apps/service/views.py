from django.shortcuts import render,get_object_or_404
from .models import Service


# Create your views here.
def service(request):
    services = Service.objects.all()
    context = {'title': 'Service', 'show_contact_section': True, 'services': services}
    return render(request, 'service/service.html', context)


def serviceDetails(request, slug):
    service = get_object_or_404(Service, service_slug=slug)
    context = {'title': service.service_title, 'show_contact_section': True, 'service': service}
    return render(request, 'service/serviceDetails.html', context)


def servicePortfolio(request):
    context = {'title': 'Service Portfolio', 'show_contact_section': True}
    return render(request, 'service/servicePortfolio.html', context)
