"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from games.views import home_page, about_page, product_page, contact_page, remot_page, video_page

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='home'),
    path('redirect/', RedirectView.as_view(url='/')),
]



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('product/', product_page, name='product'),
    path('contact/', contact_page, name='contact'),
    path('remot/', remot_page, name='remot'),
    path('video/', video_page, name='video'),
    path('', product_page, name='game_list')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)