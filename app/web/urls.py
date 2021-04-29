from django.urls import path
from django.conf.urls import url, include
from . import views
from django.views.generic import TemplateView


urlpatterns = [
	path('main/', views.index, name = 'index'),
	#path('install/', views.install, name = 'install'),
	#path('support/', views.index, name = 'support'),
	#path('users/<int:user_id>', views.user, name = 'user'),
	#path('users/<int:user_id>/<int:device_id>/', views.device, name = 'device'),
	path('login/', views.loginPage, name = 'login'),
	path('register/', views.registerPage, name = 'register'),
	path('logout/', views.logoutUser, name='logout'),
]
