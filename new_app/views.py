from django.shortcuts import render,redirect
from .form import *
from django.contrib import messages

from .models import *


# Create your views here.

def index(request):
    form = Booking_f(request.POST)
    # print(request.POST)
    if request.method == 'POST':
        form = Booking_f(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Table booking has been Completed')
            return redirect('/')
        else:
            form = Booking_f()
            
            return render(request, 'new_app/index.html')


    blog_1 = blog_img_1.objects.all()
    blog_2 = blog_img_2.objects.all()
    blog_3 = blog_img_3.objects.all()

    context ={
        'form':form,
        'blog_1':blog_1,
        'blog_2':blog_2,
        'blog_3':blog_3,
    }
    return render(request, 'new_app/index.html',context)

def about(request):
    return render(request, 'new_app/about.html')

def blog_single(request):
    return render(request, 'new_app/blog-single.html')

def blog(request):
    blog_1 = blog_img_1.objects.all()
    blog_2 = blog_img_2.objects.all()
    blog_3 = blog_img_3.objects.all()

    context= {
        'blog_1':blog_1,
        'blog_2':blog_2,
        'blog_3':blog_3,
    }

    return render(request, 'new_app/blog.html', context)

def chef(request):
    form = Booking_f(request.POST)
    # print(request.POST)
    if request.method == 'POST':
        form = Booking_f(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Table booking has been Completed')
            return redirect('/')
        else:
            form = Booking_f()
            
            return render(request, 'new_app/chef.html')
    context ={
        'form':form,
    }
    return render(request, 'new_app/chef.html',context)

def contact(request):
    form = Contact_f(request.POST)
    # print(request.POST)
    if request.method == 'POST':
        form = Contact_f(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Message has been sent!')
            return redirect('/')
        else:
            form = Contact_f()
            
            return render(request, 'new_app/contact.html')
    context ={
        'form':form,
    }
    return render(request, 'new_app/contact.html',context)

def menu(request):
    form = Booking_f(request.POST)
    # print(request.POST)
    if request.method == 'POST':
        form = Booking_f(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Table booking has been Completed')
            return redirect('/')
        else:
            form = Booking_f()
            
            return render(request, 'new_app/menu.html')
    context ={
        'form':form,
    }
    return render(request, 'new_app/menu.html',context)

def reservation(request):
    form = Booking_f(request.POST)
    # print(request.POST)
    if request.method == 'POST':
        form = Booking_f(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Table booking has been Completed')
            return redirect('/')
        else:
            form = Booking_f()
            
            return render(request, 'new_app/reservation.html')
    context ={
        'form':form,
    }
    return render(request, 'new_app/reservation.html',context)


