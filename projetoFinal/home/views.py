from django.contrib.auth import logout
from django.shortcuts import redirect, render

# Create your views here.


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    logout(request)
    return redirect(home)
