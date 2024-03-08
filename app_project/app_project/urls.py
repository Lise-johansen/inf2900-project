"""
URL configuration for app_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from airfinn import views
from airfinn import utils
from django.urls import path, include  # Ensure include is imported
from django.conf.urls.static import static
from django.conf import settings

appname = 'app_project'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/login/', views.login, name='login'),
    path('api/register/', views.register, name='register'),
    path('api/send-password-reset-email/',
         views.send_password_reset_email, name='send_password_reset_email'),
    path('api/reset-password/<str:uidb64>/<str:token>/', views.reset_password, name='reset_password'),
    path('api/dashboard/', views.dashboard, name='dashboard'),
    path('api/search/', views.search_items, name='search_items'),
    path('api/logout/', views.logout, name='logout'),
    path('api/upload-profile-picture/', utils.upload_profile_picture, name='upload_profile_picture'),
    path('api/verify-email/', views.verify_email, name='verify_email'),
    path('api/create-item/', views.create_item, name='create_item'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
