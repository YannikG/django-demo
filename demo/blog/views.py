from django.shortcuts import render
from blog.models import BlogPost, BlogThread
from blog.forms import BlogThreadForm
# Create your views here.
def blog_index(request):
    query_form = BlogThreadForm(request.GET)
    if (query_form.is_valid() and query_form.cleaned_data["blog_thread"] is not None):
        posts_list = BlogPost.objects.filter(blog_thread=query_form.cleaned_data["blog_thread"])
    else:
        posts_list = BlogPost.objects.all()

    return(render(request, "blog_index.html", {
        "form": query_form,
        "posts": posts_list
    }))

def blog_details(request, id):
    post = BlogPost.objects.get(pk=id)
    return(render(request, "blog_details.html", {
        "post": post
    }))