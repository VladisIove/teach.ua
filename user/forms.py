from django import forms 

from django_registration.forms import RegistrationFormUniqueEmail

from .models import User 

class CustomFormRegistration(RegistrationFormUniqueEmail):

	class Meta():
		model = User 
		fields = ('name', 'surname','email', 'password1', 'password2', 'type_persone',)


class HelpForm( forms.Form ):
	name = forms.CharField(max_length=120, help_text='Имя и Фамилия')
	email = forms.EmailField( max_length = 200)
	message = forms.CharField(widget = forms.Textarea)