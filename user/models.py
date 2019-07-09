from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.





class User(AbstractUser):
	name = models.CharField(max_length=120, blank=False, null=False)
	surname = models.CharField(max_length=120, blank=False, null=False)
	slug = models.SlugField(max_length=240, blank=False, null=False, unique=True)
	email = models.EmailField(max_length=120, blank=False, null=False, unique=True)
	mobile_number = models.CharField(max_length=20, blank=True, null=True)
	img = models.ImageField(upload_to = 'img_user/', blank=False, null=False)
	about = models.TextField(max_length=500)
	age = models.PositiveSmallIntegerField(null=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	price_per_hource = models.PositiveSmallIntegerField

	TEACHER = 'T'
	STUDENT = 'S'
	TYPE_PERSONE = (
		(TEACHER, 'teacher'),
		(STUDENT, 'student'),
		)
	type_persone = models.CharField(choices=TYPE_PERSONE, max_length=1, default=STUDENT)

	skype = models.CharField(max_length=120, blank=True, null=True)
	telegram = models.CharField(max_length=120, blank=True, null=True)
	viber = models.CharField(max_length=120, blank=True, null=True)
	instagram = models.CharField(max_length=120, blank=True, null=True)

	type_lesson = models.ManyToManyField('TypeLesson', related_name='typelesson')

	skill = models.ManyToManyField('Skill', related_name='skill')

	like = models.ManyToManyField('Like', related_name='like')

	comment = models.ManyToManyField('Comment', related_name='comment')

	create_time = models.DateTimeField(auto_now_add=True)


	# I am xz kak realizovat podpicky
	start_subscription = models.DateTimeField(null=True)
	end_subscription = models.DateTimeField(null=True)
	subscription = models.BooleanField(default=False, null=False)

	def __str__(self):
		return 'User: {} {} , type: {}, sub: {}'.format(self.name, self.surname, self.type_persone, self.subscription)

	class Meta:
		ordering = ['name', 'subscription']

class TypeLesson(models.Model):
	type_lesson = models.CharField(max_length=120, blank=False, null=False)

class Skill(models.Model):
	skill_name = models.CharField(max_length=120, blank=False, null=False)
	
class Like(models.Model):
	raiting = models.PositiveSmallIntegerField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_like')

class Comment(models.Model):
	text = models.TextField(max_length=500)
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_comment')
	date = models.DateTimeField(auto_now_add=True)