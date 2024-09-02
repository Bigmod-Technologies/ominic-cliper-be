from django.shortcuts import render


# Create your views here.
def home(request):
    context = {'title': 'Omnic Clipper', 'show_contact_section': True}
    return render(request, 'index.html', context)


def blog(request):
    context = {'title': 'Blog', 'show_contact_section': True}
    return render(request, 'blog/blog.html', context)


def blogDetails(request):
    context = {'title': 'Blog Details', 'show_contact_section': True}
    return render(request, 'blog/blogDetails.html', context)


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
    context = {'title': 'Error', 'show_contact_section': False, 'contact_url': True}
    return render(request, 'others/error.html', context)


def order(request):
    context = {'title': 'Order', 'show_contact_section': False, 'contact_url': True}
    return render(request, 'pricing/order.html', context)


def pricingImage(request):
    context = {'title': 'Pricing Image', 'show_contact_section': True}
    return render(request, 'pricing/pricingImage.html', context)
