from django.shortcuts import render
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView

from .models import User 
# Create your views here.




class HomePageView(ListView):
	template_name = 'home.html'
	context_object_name = 'users'
	model = User

	def get_queryset(self):
		if self.request.user.type_persone == 'S':
			users = User.objects.filter(type_persone = 'T')
		else:
			user = User.objects.filter(type_persone = 'S')
		return users


class DetailUserView(DetailView):
	model = User 
	template_name = 'detail_user_profile.html'
	
'''
class Registration():


class Login():



'''