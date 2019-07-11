from django.shortcuts import render, redirect 
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.list import ListView 
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from .models import User, TypeLesson
from .forms import HelpForm, UpdateUserProfile
# Create your views here.




class HomePageView(ListView):
	template_name = 'home.html'
	context_object_name = 'users'
	model = User

	def get_queryset(self):
		try:
			if self.request.user.type_persone == 'S':
				users = User.objects.filter(type_persone = 'T')
			else:
				users = User.objects.filter(type_persone = 'S')
		except:
			users = User.objects.all().exclude(is_staff = True)

		return users

class ProfileUpdateView(UpdateView, LoginRequiredMixin):
	template_name = 'profile.html'
	form_class = UpdateUserProfile 
	model = User

	def form_valid(self, form):
		obj = form.save(commit=True)
		obj.last_change = timezone.now()
		obj.save()
		return HttpResponseRedirect(self.request.path_info)

	def dispatch(self, request, *args, **kwargs):
		"""Return 403 if flag is not set in a user profile. """
		if request.user.pk == kwargs['pk']:
			return super().dispatch(request, *args, **kwargs)
		return redirect('user:home')
		




def help_message(request):
	if request.method == 'POST':
		form = HelpForm( request.POST )

		if form.is_valid():
			current_site = get_current_site(request)
			mail_subject = 'Пришло письмо с поддержки'
			message = request.POST.get('email') + ' ' + request.POST.get('name') +' '+ request.POST.get('message')
			to_email = 'vlad.shelemakha0302@gmail.com'
			email = EmailMessage( mail_subject, message, to = [to_email] )
			email.send()	
			message = 'Письмо отправлено'
			messages.success(request, message) 
			return render(request, 'help.html', {'form': form})
			#return HttpResponse('Письмо отправлено')	
	else:
		form = HelpForm()

	return render(request, 'help.html', {'form': form})