from django import forms 
from django.contrib.auth.forms import UserCreationForm

from .models import User 




class FormRegistration(UserCreationForm):
	name = forms.CharField(required=True, label='Имя',  max_length=100)
	surname = forms.CharField(required=True, label='Фамилия', max_length=100)
	email = forms.CharField(required=True, label='E-mail',  max_length=100)

	def __init__(self, *args, **kwargs):
		super(FormRegistration, self).__init__(*args, **kwargs)

		for fieldname in ['password1', 'password2']:
			self.fields[fieldname].help_text = None

	class Meta():
		model = User 
		fields = ('name', 'surname','email', 'password1', 'password2', 'type_persone',)



class HelpForm( forms.Form ):
	name = forms.CharField(max_length=120, help_text='Имя и Фамилия')
	email = forms.EmailField( max_length = 200)
	message = forms.CharField(widget = forms.Textarea)

