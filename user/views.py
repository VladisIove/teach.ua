# Create your views here.
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from social_django.models import UserSocialAuth
import json 
import os
from django.urls import reverse_lazy
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework import mixins, generics, permissions, viewsets
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from django.core import signing
from django_registration import signals
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import requires_csrf_token
from teach import settings 

from django.core.mail import EmailMessage
from django.contrib import messages


from .forms import HelpForm, UpdateUserProfile, FilterForm, FormRegistration
from .models import User, Comment, TypeLesson, Skill
from .serializers import Userserializer, UserProfileSerializer
from .permissions import IsOwnerOrReadOnly

from .tasks import send_activation_email

from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from .tokens import account_activation_token

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string

from django.core.mail import EmailMessage




def usersignup(request):
	if request.method == 'POST':
		form = FormRegistration(request.POST)
		if form.is_valid():
			user = form.save(commit = False)
			user.is_active = False 
			user.save()
			domain_site = get_current_site(request).domain
			to_email = form.cleaned_data.get('email')
			uid = urlsafe_base64_encode(force_bytes(user.pk))
			token = account_activation_token.make_token(user)
			send_activation_email.delay(domain_site, user.name, to_email, uid, token)
			return render(request, 'django_registration/registration_complete.html')
	else:
		form = FormRegistration()
	return render(request, 'django_registration/registration_form.html', {'form': form})


def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'django_registration/activation_complete.html')
    else:
        return render(request, 'django_registration/activation_failed.html') 

class UserProfailView( mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
	queryset = User.objects.all()
	serializer_class = UserProfileSerializer
	parser_classes = (FormParser, JSONParser, MultiPartParser)
	#permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)


	def put(self, request, *args, **kwargs):

		try:
			user = User.objects.get(email = request.data['email'])
			user_up = User.objects.filter(email = request.data['email'])
		except User.DoesNotExist:
			return Response({'data': 'fail'}, status = status.HTTP_400_BAD_REQUEST)
		
		if request.FILES:
			return self.update(request, *args, **kwargs)

		user.type_lesson.clear()
		for type_lesson_id in request.data['type_lesson']:
			user.type_lesson.add(TypeLesson.objects.get(id = type_lesson_id))
		user.skill.clear()
		for skill_name in request.data['skill']:
			obj, _ =Skill.objects.get_or_create(skill_name = skill_name)
			user.skill.add(obj)
		user_up.update(name = request.data['name'], 
				surname=request.data['surname'],
				mobile_number=request.data['mobile_number'],
				about=request.data['about'],
				age=request.data['age'],
				price_per_hource=request.data['price_per_hource'],
				city=request.data['city'],
				skype=request.data['skype'],
				instagram=request.data['instagram'],
				telegram=request.data['telegram'],
				viber=request.data['viber'],
				valid_announcement=request.data['valid_announcement'])


		return Response({'data': 'good'}, status = status.HTTP_200_OK)





@login_required
def settings(request):
	user = request.user

	try:
		github_login = user.social_auth.get(provider='github')
	except UserSocialAuth.DoesNotExist:
		github_login = None

	# try:
	#     twitter_login = user.social_auth.get(provider='twitter')
	# except UserSocialAuth.DoesNotExist:
	#     twitter_login = None
	#
	#try:
	#    facebook_login = user.social_auth.get(provider='facebook')
	#except UserSocialAuth.DoesNotExist:
	#   facebook_login = None

	can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

	return render(request, 'settings.html', {
		'github_login': github_login,
		# 'twitter_login': twitter_login,
		#'facebook_login': facebook_login,
		'can_disconnect': can_disconnect
	})


@login_required
def password(request):
	if request.user.has_usable_password():
		PasswordForm = PasswordChangeForm
	else:
		PasswordForm = AdminPasswordChangeForm

	if request.method == 'POST':
		form = PasswordForm(request.user, request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, 'Your password was successfully updated!')
			return redirect('user:password')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordForm(request.user)
	return render(request, 'password.html', {'form': form})




class UserView(APIView):

	def get(self, request):
		users = User.objects.filter(valid_announcement = True).exclude(id = request.user.id)
		serializer = Userserializer(users, many = True)
		return Response({'data': serializer.data })

class HomePageView(TemplateView):
	template_name = 'home.html'


class ProfileUpdateView(TemplateView, LoginRequiredMixin):
	template_name = 'profile.html'

	def dispatch(self, request, *args, **kwargs):
		"""Return 403 if flag is not set in a user profile. """

		if request.user.pk == kwargs['pk']:
			return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)
		return redirect('user:home')


def help_message(request):
	if request.method == 'POST':
		form = HelpForm(request.POST)

		if form.is_valid():
			current_site = get_current_site(request)
			mail_subject = 'Пришло письмо с поддержки'
			message = request.POST.get('email') + ' ' + request.POST.get('name') + ' ' + request.POST.get('message')
			to_email = 'teach.teacher.ua@gmail.com'
			email = EmailMessage(mail_subject, message, to=[to_email])
			email.send()
			message = 'Письмо отправлено'
			messages.success(request, message)
			return render(request, 'help.html', {'form': form})
	# return HttpResponse('Письмо отправлено')
	else:
		form = HelpForm()

	return render(request, 'help.html', {'form': form})


@csrf_exempt
def add_like(request):
	print(request.POST)
	us_id = request.POST.get('profile_id')
	pr_id = request.POST.get('user_id')
	user_who_add = User.objects.get(id=pr_id)
	user_then_add = User.objects.get(id=us_id)
	if user_who_add in user_then_add.like.all():
		user_then_add.like.remove(user_who_add)
	else:
		user_then_add.like.add(user_who_add)
	return JsonResponse({'status': 1, 'data': user_then_add.id, 'like': user_then_add.like.count()})



@csrf_exempt
def add_comment(request):
	us_id = request.POST.get('user_id')
	pr_id = request.POST.get('profile_id')
	user_who_add = User.objects.get(id=pr_id)
	user_then_add = User.objects.get(id=us_id)

	comment = Comment.objects.create(text=request.POST.get('text'), owner=user_who_add, recipient=user_then_add)
	return JsonResponse({'status': 1, 'data': user_then_add.id, 'comment': comment.text, 'owner_name': user_who_add.name,'owner_surname': user_who_add.surname , 'date': comment.date})

