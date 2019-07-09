from django.urls import path 

from .views import HomePageView, DetailUserView

app_name = 'user'

urlpatterns = [

	path('home/', HomePageView.as_view(), name='home'),
	path('profile/<slug:slug>', DetailUserView.as_view(), name='detail_user_profile')
	#path('registration/'),
	#path('login/'),
	#path('foget_password_email/'),
	#path('foget_password_reset/'),
	#path('profile/'),
	#path('add_status/'),

]