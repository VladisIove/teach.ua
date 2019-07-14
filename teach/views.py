from django.shortcuts import redirect


def RedirectToHomePage(request):
	print('redirect')
	print('redirect')
	print('redirect')
	print('redirect')
	return redirect('user:home')