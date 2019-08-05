from django import forms 
from django.contrib.auth.forms import UserCreationForm

from django_registration.forms import RegistrationFormUniqueEmail

from .models import User , TypeLesson, Skill




class FormRegistration(UserCreationForm):
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

	about = forms.CharField(required=True, label='О себе:', widget=forms.Textarea)

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


class FilterForm( forms.Form ):

	min_age = forms.IntegerField(label='Минимальный возраст', required=False, widget=forms.TextInput(attrs={'placeholder': '12'}))
	max_age = forms.IntegerField(label='Максимальный возраст', required=False, widget=forms.TextInput(attrs={'placeholder': '90'}))
	min_salary = forms.IntegerField(label='Минимальтая плата в час', required=False, widget=forms.TextInput(attrs={'placeholder': '0'}))
	max_salary = forms.IntegerField(label='Максимальная плата в час', required=False, widget=forms.TextInput(attrs={'placeholder': '200'}))
	city = forms.CharField(label='Город', required=False, widget=forms.TextInput(attrs={'placeholder': 'Search'}))
	type_work = forms.ModelMultipleChoiceField(label = 'Вид занятости:',queryset=TypeLesson.objects.all(),
												widget=forms.CheckboxSelectMultiple,required=False)
	name_skill = forms.CharField(label='Название предмета', required=False, widget=forms.TextInput(attrs={'placeholder': 'Математика'}))
	# rating = forms.BooleanField(label='Фильтровать по рейтингу', required=False) Dont working, becouse not like 
	#comment = forms.BooleanField(label='Есть комментарии у пользователя', required=False) Dont working, becouse not comment