from django.urls import path, include, re_path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django_registration.views import ActivationView
from django.contrib.auth.decorators import login_required 
from .views import (usersignup, 
					activate_account, 
					UserProfailView, 
					HomePageView,
					ProfileUpdateView, 
	 				help_message,
	  				settings,
	  				password,
	    			add_like,
	     			add_comment,
	      			UserView)

app_name = 'user'

urlpatterns = [
	path('home/', HomePageView.as_view(), name='home'),
	#path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
	path('users/', UserView.as_view(), name='users'),
	path('user_profile/<int:pk>/', csrf_exempt(UserProfailView.as_view()), name='user_profile'),
	path('profile/<int:pk>/', login_required(ProfileUpdateView.as_view()), name='update_profile'),
	path('subscribe/', TemplateView.as_view(template_name='subscribe.html'), name='subscribe'),
	path('help/', help_message, name='help'),
	path('settings/', settings, name='settings'),
	path('settings/password/', password, name='password'),
	path('add_like/', add_like, name='add-like'),
	path('add_comment/', add_comment, name='add-comment'),
	path('signup/', usersignup, name='django_registration_register'),
	re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate_account, name='activate_account'),
]