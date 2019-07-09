from django.urls import path, include

from .views import HomePageView, ProfileUpdateView

app_name = 'user'

urlpatterns = [
	path('home/', HomePageView.as_view(), name='home'),
	path('profile/<int:pk>/',ProfileUpdateView.as_view(), name='update_profile')
	#path('profile/'),
	#path('add_status/'),

]