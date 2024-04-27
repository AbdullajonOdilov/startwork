from django.shortcuts import render
from .models import Portfolio, Testimonials, Stats

def home(request):
    portfolios = Portfolio.objects.all()
    testimonials = Testimonials.objects.all()
    stats = Stats.objects.first()  # Assuming you have only one Stats object

    context = {
        'portfolios': portfolios,
        'testimonials': testimonials,
        'stats': stats,
    }
    return render(request, 'portfolio/index.html', context)
