from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index_page'),
    path('blog-single',blog_single,name='blog-single'),
    path('blog',blog,name='blog'),
    path('chef',chef,name='chef'),
    path('contact',contact,name='contact'),
    path('about',about,name='about'),
    path('menu',menu,name='menu'),
    path('reservation',reservation,name='reservation'),
]
