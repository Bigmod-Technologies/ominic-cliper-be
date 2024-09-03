from django.shortcuts import render


# Create your views here.

def blog(request):
    context = {'title': 'Blog', 'show_contact_section': True}
    return render(request, 'blog/blog.html', context)


def blogDetails(request):
    context = {'title': 'Blog Details', 'show_contact_section': True}
    return render(request, 'blog/blogDetails.html', context)
