from django.urls import path, include

from .views import HomePageView

app_name = 'user'

urlpatterns = [

	path('home/', HomePageView.as_view(), name='home'),
	path('', include('django.contrib.auth.urls')),
	#path('registration/'),
	#path('login/'),
	#path('foget_password_email/'),
	#path('foget_password_reset/'),
	#path('profile/'),
	#path('add_status/'),

]