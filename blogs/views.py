from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import BlogPost
from .forms import BlogForm

# Create your views here.
def index(request):
    '''The home page for blog and shows all posts'''
    posts = BlogPost.objects.order_by('-date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)

@login_required
def new_blog(request):
    """Add a new blog"""
    if request.method != 'POST':
        #No data submitted, create blank form
        form = BlogForm()
    else:
        # POST data received, process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            new_blog = form.save(commit=False)
            new_blog.owner = request.user
            new_blog.save()
            return redirect('blogs:index')

    #display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def edit_blog(request, blog_id):
    """Edit existing blog"""
    blog = BlogPost.objects.get(id=blog_id)

    check_post_owner(blog, request)

    if request.method != 'POST':
        # Inital request; prefill form with current post
        form = BlogForm(instance=blog)
    else:
        # POST data submitted; process data
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')  #Could be wrong but we'll see!
            
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)

def check_post_owner(blog, request):
    if blog.owner != request.user:
        raise Http404

