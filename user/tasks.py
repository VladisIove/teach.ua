from celery import task

from django.core.mail import EmailMessage
from celery.task.schedules import crontab

from django.template.loader import render_to_string
 

@task 
def help_message_task(email, name, message):
	
	#Task to send an help e-mail .
	
	mail_subject = 'Пришло письмо с поддержки'
	message = email + '\n ' + name + '\n ' + message
	to_email = 'teach.teacher.ua@gmail.com'
	email = EmailMessage(mail_subject, message, to=[to_email])
	email.send()
	return email




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
