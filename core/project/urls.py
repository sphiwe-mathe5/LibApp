from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import index, contact, services, about, enquire
from django.conf.urls.static import static




urlpatterns = [
    path('', index, name='index'),
    path('items/', include('item.urls')),
    path('admin/', admin.site.urls),
    path('contact/', contact, name='contact'),
    path('services/', services, name='services'),
    path('about/', about, name='about'),
    path('', include('newsletter.urls')),
    path('enquire/', enquire, name='enquire'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_URL)
