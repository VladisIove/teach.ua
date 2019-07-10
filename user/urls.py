from django.urls import path, include
from django.views.generic.base import TemplateView

from .views import HomePageView, ProfileUpdateView, help_message

app_name = 'user'

urlpatterns = [
	path('home/', HomePageView.as_view(), name='home'),
	path('profile/<int:pk>/',ProfileUpdateView.as_view(), name='update_profile'),
	path('subscribe/', TemplateView.as_view(template_name='subscribe.html'), name='subscribe'),
	path('help/', help_message, name='help'),
	#path('add_status/'),

]