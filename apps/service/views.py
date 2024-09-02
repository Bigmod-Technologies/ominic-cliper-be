from django.shortcuts import render


# Create your views here.
def service(request):
    context = {'title': 'Service', 'show_contact_section': True}
    return render(request, 'service/service.html', context)


def serviceDetails(request):
    context = {'title': 'Service Details', 'show_contact_section': True}
    return render(request, 'service/serviceDetails.html', context)


def servicePortfolio(request):
    context = {'title': 'Service Portfolio', 'show_contact_section': True}
    return render(request, 'service/servicePortfolio.html', context)
