from django import forms 

from django_registration.forms import RegistrationFormUniqueEmail

from .models import User 

class CustomFormRegistration(RegistrationFormUniqueEmail):

	class Meta():
		model = User 
		fields = ('name', 'surname','email', 'password1', 'password2', 'type_persone',)