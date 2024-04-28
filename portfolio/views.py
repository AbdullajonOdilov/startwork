from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_as, logout as logout_as
from .models import Portfolio, Testimonials, Stats
from django.contrib import messages
from startteam.models import User

def home(request):
    portfolios = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()


    context = {
        'portfolios': portfolios,
        'testimonials': testimonials,

    }
    return render(request, 'portfolio/index.html', context)

def login(request):
    if request.user.is_authenticated: return redirect('work:index')
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)
            if user is not None:
                if user.is_active:
                    login_as(request, user)
                    return redirect('work:index')
                else:
                    messages.error(request, 'Xatolik yuz berdi')
                    response = redirect('portfolio:login')
                    return response
            else:
                messages.error(request, 'Login yoki parolda xatolik bor')
                response = redirect('portfolio:login')
                return response
        except Exception as e:
            print(e)
    return render(request, 'portfolio/login.html')

def signup(request):
    if request.user.is_authenticated: return redirect('work:index')
    if request.method == "POST":
        try:
            full_name = request.POST.get('full_name')
            username = request.POST.get('username')
            password = request.POST.get('password')
            position = request.POST.get('position')
            edu = request.POST.get('edu')
            contact = request.POST.get('contact')
            skills = request.POST.get('skills')
            address = request.POST.get('address')
            user = User.objects.create_user(username=username, password=password, full_name=full_name, position=position,
                                             education=edu, contacts=contact, skills=skills, address=address)
            # Authenticate and login the user
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_active:
                login_as(request, user)
                return redirect('work:index')
            else:
                messages.error(request, 'Xatolik yuz berdi')
                return redirect('portfolio:login')
        except Exception as e:
            print(e)
            messages.error(request, 'Xatolik yuz berdi')
            return redirect('portfolio:login')

    return render(request, 'portfolio/sign.html')