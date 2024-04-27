from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logout_user(request):
    logout(request)
    response = redirect('/')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response
