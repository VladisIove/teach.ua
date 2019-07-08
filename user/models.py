from django.db import models

# Create your models here.





class User(models.Model):
	name = models.CharField(max_length=120, blank=False, null=False)
	surname = models.CharField(max_length=120, blank=False, null=False)
	slug = models.SlugField(max_length=240, blank=False, null=False)
	email = models.EmailField(max_length=120, blank=False, null=False, unique=True)
	mobile_number = models.CharField(max_length=20, blank=True, null=True)
	img = models.ImageField(upload_to = 'img_user/', blank=False, null=False)
	about = models.TextField(max_length=500)
	age = models.PositiveSmallIntegerField()
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

	skill = models.ManyToManyField(Skill)

	like = models.ManyToManyField(Like)

	comment = models.ManyToManyField(Comment)

	create_time = models.DateTimeField(auto_now_add=True)
	# I am xz kak realizovat podpicky
	start_subscription = models.DateTimeField()
	end_subscription = models.DateTimeField()
	subscription = models.BooleanField(default=False, null=False)

	def __str__(self):
		return 'User: {} {} , type: {}, sub: {}'.format(self.name, self.surname, self.type_persone, self.subscription)

	class Meta:
		ordering = ['name', 'subscription', 'like']



class Skill(models.Model):
	skill_name = models.CharField(max_length=120, blank=False, null=False)
	
class Like(models.Model):
	raiting = models.PositiveSmallIntegerField()
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
	text = models.TextField(max_length=500)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)