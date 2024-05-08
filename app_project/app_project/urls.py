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
    path('api/send-password-reset-email/', views.send_password_reset_email, name='send_password_reset_email'),
    path('api/reset-password/<str:uidb64>/<str:token>/', views.reset_password, name='reset_password'),
    path('api/dashboard/', views.dashboard, name='dashboard'),
    path('api/search/', views.search_items, name='search_items'),
    path('api/search-page/', views.search_page, name='search_page'),
    path('api/logout/', views.logout, name='logout'),
    path('api/upload-profile-picture/', utils.upload_profile_picture, name='upload_profile_picture'),
    path('api/verify-email/', views.verify_email, name='verify_email'),
    path('api/edit_listing/<int:item_id>/', views.edit_listing, name='edit_listing'),
    path('api/delete_item/<int:item_id>', views.delete_listing, name='delete_listing'),
    path('api/contact_us_message/', views.contact_us_message, name='contact_us_message'),
    path('api/update_user/', views.update_user, name='update_user'),
    path('api/delete_user/', views.delete_user, name='delete_user'),
    path('api/get_items/<str:category>', views.get_listings, name='get_listings'),
    path('api/get-conversations/', views.get_conversations, name='get_conversations'),
    path('api/delete-conversation/<int:conversation_id>/', views.delete_conversation, name='delete_conversation'),
    path('api/get-messages/', views.get_messages, name='get_messages'),
    path('api/send-messages/', views.send_messages, name='send_messages'),
    path('api/create-item/', views.create_item, name='create_item'),
    path('api/get_listing/<int:item_id>/', views.get_listing, name='get_listing'),
    path('api/upload_image/', views.upload_image, name='upload_image'),
    path('api/ordered-listings/', views.reserved_listings, name='reserved_listings'),
    path('api/add-favourites/', views.add_favourites, name='add_to_favourites'),
    path('api/get-favourites/', views.get_favourites, name='get_favourites'),
    path('api/remove-from-favourites/<int:item_id>/', views.remove_favourites, name='remove_favourites'),
    path('api/reserved-dates/<int:listing>/', views.get_reserved_dates, name='get_reserved_dates'),
    path('api/order-listing/<int:listing>/', views.order_listing, name='order_listing'),
    path('api/verify-user/', views.verify_user, name='verify_user'),
    path('api/get-user/', views.get_user, name='get_user'),
    path('api/get-user-listings/', views.get_user_listings, name='get_user_listings'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
