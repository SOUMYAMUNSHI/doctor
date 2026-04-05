from django.shortcuts import render

# Create your views here.

from .models import Blog

def blog_list(request):

    blogs = Blog.objects.all().order_by('-created_at')

    return render(request,"blogs.html",{"blogs":blogs})