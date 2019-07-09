from django.shortcuts import render
from django.views.generic import View
from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView

from .models import User 
# Create your views here.




class HomePageView(ListView):
	template_name = 'home.html'
	context_object_name = 'users'
	model = User

	def get_queryset(self):
		try:
			if self.request.user.type_persone == 'S':
				users = User.objects.filter(type_persone = 'T')
			else:
				users = User.objects.filter(type_persone = 'S')
		except:
			users = User.objects.all().exclude(is_staff = True)

		return users

#class LogoutView(View)
	
'''
class Registration():


class Login():



'''