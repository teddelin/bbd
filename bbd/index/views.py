from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from bbd import settings
from django.contrib.auth.decorators import login_required

def Login(request):
	next = request.GET.get('next', '/home/')
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				HttpResponse("Inactive user.")
		else:
			HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "index/login.html", {'redirect_to': next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

@login_required
def Home(request):
	return render(request, "index/home.html", {})