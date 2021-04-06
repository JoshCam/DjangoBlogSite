from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogForm

# Create your views here.
def index(request):
    '''The home page for blog and shows all posts'''
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blogs/index.html', context)


def new_blog(request):
    """Add a new blog"""
    if request.method != 'POST':
        #No data submitted, create blank form
        form = BlogForm()
    else:
        # POST data received, process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')  #This might cause an error, not sure what 'blogs:index' does

    #display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)
