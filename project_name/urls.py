"""{{ project_name }} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
"""
# Django imports
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    # Examples:
    # path('', '{{ project_name }}.views.home', name='home'),
    # path('blog/', include('blog.urls', namespace='blog')),

    # provide the most basic login/logout functionality
    path('accounts/', include('django.contrib.auth.urls')),

    # enable the admin interface
    path('admin/', admin.site.urls),
]
