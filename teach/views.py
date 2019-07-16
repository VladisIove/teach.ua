from django.shortcuts import redirect


def RedirectToHomePage(request):
	return redirect('user:home')