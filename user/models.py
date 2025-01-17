from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

import json 
from datetime import datetime
# Create your models here.


class UserManager(BaseUserManager):
	"""Define a model manager for User model with no username field."""

	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		"""Create and save a User with the given email and password."""
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		"""Create and save a regular User with the given email and password."""
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		"""Create and save a SuperUser with the given email and password."""
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')

		return self._create_user(email, password, **extra_fields)




class User(AbstractUser):
	username = None 
	name = models.CharField(max_length=120, blank=True, null=True, verbose_name='Имя')
	surname = models.CharField(max_length=120, blank=True, null=True, verbose_name='Фамилия')
	email = models.EmailField(max_length=120, blank=False, null=False, unique=True, verbose_name='Email')
	valid_announcement = models.BooleanField(default=False, verbose_name='Показывать ваш профиль другим пользователям?')

	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this admin site.'),
		)
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
			'Designates whether this user should be treated as active. ''Unselect this instead of deleting accounts.'
			),
		)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()

	mobile_number = models.CharField(max_length=20, blank=True, null=True, verbose_name='Номер телефона')
	img = models.ImageField(upload_to = 'media/', verbose_name='Фотография профиля', default='../static/img/noimage.jpg')
	#img = models.URLField( verbose_name='Фотография профиля', default='../static/img/noimage.jpg')
	about = models.TextField(max_length=140, verbose_name='О вас:', blank=True, null=True)
	age = models.PositiveSmallIntegerField(null=True , verbose_name='Возраст', blank=True)
	city = models.CharField(max_length=50, blank=True, null=True , verbose_name='Город')
	price_per_hource = models.PositiveSmallIntegerField(default=0, verbose_name='Цена в час', blank=True, null=True)


	TEACHER = 'T'
	STUDENT = 'S'
	TYPE_PERSONE = (
		(TEACHER, 'Преподователь'),
		(STUDENT, 'Ученик'),
		)
	type_persone = models.CharField(choices=TYPE_PERSONE, max_length=1, default=STUDENT, verbose_name='Кем хотите быть на teach.ua')

	skype = models.CharField(max_length=120, blank=True, null=True, verbose_name='Skype')
	telegram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Telegram')
	viber = models.CharField(max_length=120, blank=True, null=True, verbose_name='Viber')
	instagram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Instagram')

	type_lesson = models.ManyToManyField('TypeLesson', related_name='typelesson' ,blank=True, verbose_name='Вид преподования')

	skill = models.ManyToManyField('Skill', related_name='skill',blank=True, verbose_name='Предмет')

	like = models.ManyToManyField('self', related_name='like', blank=True)

	create_time = models.DateTimeField(auto_now_add=True)
	last_change = models.DateTimeField(blank=True, null=True)

	# I am xz kak realizovat podpicky
	start_subscription = models.DateTimeField(blank=True, null=True)
	LOW = 'L'
	MIDDLE = 'M'
	VIP = 'V'
	SUBSCRIPTION = (
		(LOW, 'low'),
		(MIDDLE, 'middle'),
		(VIP, 'vip') ,
		)
	subscription = models.CharField(choices=SUBSCRIPTION, max_length=1, default=LOW)

	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.email], **kwargs)

		
	def get_absolute_url(self):
		return reverse('user:update_profile', args = [self.pk])


	def __str__(self):
		return 'User: {} , type: {}, sub: {}'.format(self.name, self.surname, self.type_persone)

	class Meta:
		ordering = ['name', 'subscription']

class TypeLesson(models.Model):
	type_lesson = models.CharField(max_length=120, blank=False, null=False)

	def __str__(self):
		return f'{self.type_lesson} {self.pk}'

class Skill(models.Model):
	skill_name = models.CharField(max_length=120, blank=False, null=False)

	def __str__(self):
		return f'{self.skill_name}'
	


class Comment(models.Model):
	text = models.TextField(max_length=500, null=True, blank=True)
	recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_comment', blank=True, null=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_comment', blank=True, null=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.owner} - {self.text}'

	class Meta:
		ordering = ['-date']

