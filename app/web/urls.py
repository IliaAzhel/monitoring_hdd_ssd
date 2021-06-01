from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
	path('main/', views.index, name = 'index'),
	path('install/', views.install, name = 'install'),
	path('install/download', views.downloadZip, name = 'download'),
	path('support/', views.support, name = 'support'),
	path('user/<str:pk_test>', views.user, name = 'user'),
	path('user/devices/', views.devices, name = 'devices'),
	path('user/devices/history', views.devices, name = 'history'),
	path('login/', views.loginPage, name = 'login'),
	path('register/', views.registerPage, name = 'register'),
	path('logout/', views.logoutUser, name='logout'),
]
