from django.shortcuts import render
from .models import Portfolio, Testimonials, Stats

def home(request):
    portfolios = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()


    context = {
        'portfolios': portfolios,
        'testimonials': testimonials,

    }
    return render(request, 'portfolio/index.html', context)

<<<<<<< HEAD

def login(request):
    return render(request, 'portfolio/login.html')

def signup(request):
    return render(request, 'portfolio/sign.html')
=======
def login(request):
    return render(request, 'portfolio/login.html')
>>>>>>> origin/main
