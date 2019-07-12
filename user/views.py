from django.shortcuts import render, redirect 
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.views.generic.list import ListView 
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormMixin
from django.utils import timezone
from .models import User, TypeLesson
from .forms import HelpForm, UpdateUserProfile, FilterForm
# Create your views here.




class HomePageView(FormMixin,ListView):
	template_name = 'home.html'
	context_object_name = 'users'
	model = User
	form_class = FilterForm


	def get_queryset(self):

		if self.request.user.is_authenticated:
			if self.request.user.type_persone == 'S':
				users = User.objects.filter(type_persone = 'T', valid_announcement=False )
			else:
				users = User.objects.filter(type_persone = 'S', valid_announcement=False )
		else:
			users = User.objects.all().exclude(valid_announcement=False  )




		if self.request.GET :
			min_age = self.request.GET['min_age'] if self.request.GET['min_age'] else 0 					
			max_age = self.request.GET['max_age'] if self.request.GET['max_age'] else 110 					
			min_salary = self.request.GET['min_salary'] if self.request.GET['min_salary'] else 0 
			max_salary = self.request.GET['max_salary'] if self.request.GET['max_salary'] else 1000000  
			city = self.request.GET['city'] if self.request.GET['city'] else None 
			type_work_number = self.request.GET.getlist('type_work') if self.request.GET.getlist('type_work') else None 
			name_skill = self.request.GET['name_skill'] if self.request.GET['name_skill'] else None 

			users = users.filter(age__gte = min_age, age__lte = max_age, price_per_hource__gte = min_salary, price_per_hource__lte = max_salary )
			
			if city is not None:
				users = users.filter(city__in = city)	
			if name_skill is not None:
				users = users.filter(name_skill__in = name_skill)
			if type_work_number is not None:
				type_work = []
				user = []
				for number in type_work_number:
					type_work.append(TypeLesson.objects.get(pk = int(number)))
				
				users = users.filter(type_lesson__in = type_work).distinct()
			

		return users

class ProfileUpdateView(UpdateView, LoginRequiredMixin):
	template_name = 'profile.html'
	form_class = UpdateUserProfile 
	model = User


	def success_url(self, request, *args, **kwargs):
		pk = kwargs['pk']
		return redirect(reverse('user:update_profile', args=[pk]))

	def form_valid(self, form, *args, **kwargs):
		
		obj = form.save()
		obj.last_change = timezone.now()
		pk = obj.pk
		obj.save()
		return redirect(reverse('user:update_profile', args=[pk]))

	def dispatch(self, request, *args, **kwargs):
		"""Return 403 if flag is not set in a user profile. """
		
		if request.user.pk == kwargs['pk']:
			return super(ProfileUpdateView, self).dispatch(request, *args, **kwargs)
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