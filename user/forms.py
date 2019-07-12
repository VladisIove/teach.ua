from django import forms 
from crispy_forms.helper import FormHelper

from django_registration.forms import RegistrationFormUniqueEmail

from .models import User , TypeLesson, Skill

class CustomFormRegistration(RegistrationFormUniqueEmail):
	name = forms.CharField(required=True, label='Имя',  max_length=100)
	surname = forms.CharField(required=True, label='Фамилия', max_length=100)
	email = forms.CharField(required=True, label='E-mail',  max_length=100)

	class Meta():
		model = User 
		fields = ('name', 'surname','email', 'password1', 'password2', 'type_persone',)


class UpdateUserProfile( forms.ModelForm ):
	img = forms.ImageField(label=('Твоя фотография'),required=False, error_messages = {'invalid':("только фотографии")}, widget=forms.FileInput)

	type_lesson = forms.ModelMultipleChoiceField(
		label = 'Вид занятости:',
		queryset=TypeLesson.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False
		)

	skill = forms.ModelMultipleChoiceField(
		label = 'Предметы:',
		queryset=Skill.objects.all(),
		widget=forms.CheckboxSelectMultiple,
		required=False
		)

	email = forms.CharField(required=False,
		widget=forms.TextInput(attrs={'readonly':'readonly'})
		)

	about = forms.CharField(required=False, label='О себе:', widget=forms.Textarea)

	age = forms.CharField(required=True, label='Взораст:')

	price_per_hource = forms.CharField(required=True, label='Цена за час:')


	def __init__(self, *args, **kwargs):

		super(UpdateUserProfile, self).__init__(*args, **kwargs)

		self.fields['about'].widget.attrs['class'] = 'no-resize'

	class Meta():
		model = User 
		fields = ('name','email','last_change',
		'surname', 	'valid_announcement', 
		'mobile_number', 'img', 'about', 
		'age', 'city','price_per_hource','skype',
		'telegram',	'viber','instagram','type_lesson','skill')

class HelpForm( forms.Form ):
	name = forms.CharField(max_length=120, help_text='Имя и Фамилия')
	email = forms.EmailField( max_length = 200)
	message = forms.CharField(widget = forms.Textarea)