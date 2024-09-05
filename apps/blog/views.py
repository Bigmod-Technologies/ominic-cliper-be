from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Blog


# Create your views here.

def blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 6)  # Show 6 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'title': 'Blog', 'show_contact_section': True, 'blog': blogs, 'page_obj': page_obj}
    return render(request, 'blog/blog.html', context)


def blogDetails(request, slug):
    blogpost = get_object_or_404(Blog, blog_slug=slug)
    context = {'title': blogpost.title, 'show_contact_section': True, 'blog': blogpost}
    return render(request, 'blog/blogDetails.html', context)
