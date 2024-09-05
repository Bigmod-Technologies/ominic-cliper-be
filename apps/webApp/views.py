from django.shortcuts import render, get_object_or_404
from apps.service.models import Service
from django.conf.urls import handler404

# Create your views here.
def home(request):
    service = Service.objects.all()
    context = {'title': 'Omnic Clipper', 'show_contact_section': True, 'service': service}
    return render(request, 'index.html', context)


def termsOfService(request):
    context = {'title': 'Terms of Service', 'show_contact_section': False, 'contact_url': True}
    return render(request, 'others/405.html', context)


def privacyPolicy(request):
    context = {'title': 'Privacy Policy', 'show_contact_section': False, 'contact_url': True}
    return render(request, 'others/406.html', context)


def about(request):
    context = {'title': 'About Us', 'show_contact_section': True}
    return render(request, 'others/about.html', context)


def error(request):
    return render(request, 'others/error.html', status=404)


def order(request):
    context = {'title': 'Order', 'show_contact_section': False, 'contact_url': True}
    return render(request, 'pricing/order.html', context)


def pricingImage(request):
    context = {'title': 'Pricing Image', 'show_contact_section': True}
    return render(request, 'pricing/pricingImage.html', context)
