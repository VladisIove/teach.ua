from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required 
from .views import HomePageView, ProfileUpdateView, help_message, settings, password, add_like, add_comment

app_name = 'user'

urlpatterns = [
	path('home/', HomePageView.as_view(), name='home'),
	path('profile/<int:pk>/',login_required(ProfileUpdateView.as_view()), name='update_profile'),
	path('subscribe/', TemplateView.as_view(template_name='subscribe.html'), name='subscribe'),
	path('help/', help_message, name='help'),
	path('settings/', settings, name='settings'),
	path('settings/password/', password, name='password'),
	path('add_like/', add_like, name='add-like'),
	path('add_comment/', add_comment, name='add-comment'),

]