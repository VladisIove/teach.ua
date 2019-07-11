from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail


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
	valid_announcement = models.BooleanField(default=True, verbose_name='Показывать ваш профиль другим пользователям?')

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
	img = models.ImageField(upload_to = '', blank=False, null=False, verbose_name='Фотография профиля')
	about = models.TextField(max_length=500, verbose_name='О вас:')
	age = models.PositiveSmallIntegerField(null=True , verbose_name='Возраст')
	city = models.CharField(max_length=50, blank=True, null=True , verbose_name='Город')
	price_per_hource = models.PositiveSmallIntegerField(default=0, verbose_name='Цена в час')


	TEACHER = 'T'
	STUDENT = 'S'
	TYPE_PERSONE = (
		(TEACHER, 'teacher'),
		(STUDENT, 'student'),
		)
	type_persone = models.CharField(choices=TYPE_PERSONE, max_length=1, default=STUDENT)

	skype = models.CharField(max_length=120, blank=True, null=True, verbose_name='Skype')
	telegram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Telegram')
	viber = models.CharField(max_length=120, blank=True, null=True, verbose_name='Viber')
	instagram = models.CharField(max_length=120, blank=True, null=True, verbose_name='Instagram')

	type_lesson = models.ManyToManyField('TypeLesson', related_name='typelesson' ,blank=True, verbose_name='Вид преподования')

	skill = models.ManyToManyField('Skill', related_name='skill',blank=True, verbose_name='Предмет')

	like = models.ManyToManyField('Like', related_name='like',blank=True)

	comment = models.ManyToManyField('Comment', related_name='comment',blank=True)

	create_time = models.DateTimeField(auto_now_add=True)
	last_change = models.DateTimeField(blank=True, null=True)

	# I am xz kak realizovat podpicky
	start_subscription = models.DateTimeField(blank=True, null=True)
	end_subscription = models.DateTimeField(blank=True, null=True)
	subscription = models.BooleanField(default=False, null=False, verbose_name='Подписка')

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
		return f'{self.type_lesson}'

class Skill(models.Model):
	skill_name = models.CharField(max_length=120, blank=False, null=False)

	def __str__(self):
		return f'{self.skill_name}'
	
class Like(models.Model):
	raiting = models.PositiveSmallIntegerField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_like')

class Comment(models.Model):
	text = models.TextField(max_length=500)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_comment')
	date = models.DateTimeField(auto_now_add=True)