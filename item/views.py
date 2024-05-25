from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Category, Item
from django.http import HttpResponse
from django.urls import reverse
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category_id', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(opened=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(
        request, 'item/items.html', {
            'items': items,
            'query': query,
            'categories': categories,
            'category_id': int(category_id)
        })
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)

    return render(request, 'item/detail.html', {
        'item': item
    })

