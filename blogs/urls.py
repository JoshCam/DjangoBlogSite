"""defines URL patters for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Page for adding a new blog
    path('new_blog/', views.new_blog, name="new_blog"),
]
