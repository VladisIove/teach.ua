from celery import task
from celery.task.schedules import crontab 
from celery.decorators import periodic_task

from django.core.mail import EmailMessage
from celery.task.schedules import crontab

from django.template.loader import render_to_string

from datetime import datetime , timezone
from datetime import timedelta


from .models import User 

import pytz


@periodic_task(run_every=crontab(minute=0, hour=0), name="run_every_1_minute", ignore_result=True)
def print_user():
	utc=pytz.UTC
	date_now = datetime.now(timezone.utc)
	for user in User.objects.all():
		if user.subscription != 'L':
			if (date_now - user.start_subscription) > timedelta(days=30):
				user_up = User.objects.filter(pk = user.pk).update(subscription = 'L')

@task 
def help_message_task(email, name, message):
	
	#Task to send an help e-mail .
	
	mail_subject = 'Пришло письмо с поддержки'
	message = email + '\n ' + name + '\n ' + message
	to_email = 'teach.teacher.ua@gmail.com'
	email = EmailMessage(mail_subject, message, to=[to_email])
	email.send()





@task 
def send_activation_email(domain_site, username, to_email, uid, token):
	# Task to send activation email 

	email_subject = 'Активация аккаунта'
	message = render_to_string('activate_account.html',{
		'username': username,
		'domain': domain_site,
		'uid': uid,
		'token': token,
		})
	email = EmailMessage(email_subject, message, to=[to_email])
	email.send()
