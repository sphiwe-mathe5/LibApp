from django.shortcuts import render

from item.models import Category, Item
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings


def index(request):
    items = Item.objects.filter(opened=False) [0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories' : categories,
        'items' : items,
    })


def contact(request):
    return render(request, 'core/contact.html')


def services(request):
    items = Item.objects.filter(opened=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/services.html', {
        'categories': categories,
        'items': items,
    })


def about(request):
    return render(request, 'core/about.html',)


def enquire(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Send notification to admin
        send_mail(
            'New Service Enquiry',
            f'Name: {name}\nEmail: {email}\nPhone: {phone}\nService: {service}\nMessage: {message}',
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )

        messages.success(request, 'Your enquiry has been sent successfully!')

    return redirect('index')