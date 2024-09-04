from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.

def blog(request):
    blogs = Blog.objects.all()
    context = {'title': 'Blog', 'show_contact_section': True, 'blog': blogs}
    return render(request, 'blog/blog.html', context)


def blogDetails(request, blog_id):
    blogpost = get_object_or_404(Blog, pk=blog_id)
    context = {'title': 'Blog Details', 'show_contact_section': True, 'blog': blogpost}
    return render(request, 'blog/blogDetails.html', context)
