"""
URL configuration for chat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from base.views import home_view, register_view, login_view, friend_request_send_view,user_list_view, friend_request_list_view,friend_request_status_update_view, friend_request_delete_view, message_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('register/',register_view, name='register'),
    path('login/',login_view, name='login'),
    path('friend/request/send/', friend_request_send_view,name='friend_request_send_view'),
    path('friend/request/list/', friend_request_list_view,name='friend_request_list_view'),
    path('friend/request/status/<int:pk>/', friend_request_status_update_view,name='friend_request_status_update'),
    path('friend/request/delete/<int:pk>/', friend_request_delete_view,name='friend_request_delete'),
    path('message/view/<int:user_id>/', message_view,name='message_view'),
    path('user/list/', user_list_view,name='user_list')
]
