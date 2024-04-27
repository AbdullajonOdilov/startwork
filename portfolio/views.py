from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.translation import get_language
from portfolio.models import *
from urllib.parse import urlparse
from django.urls.base import resolve, reverse
from django.urls.exceptions import Resolver404
from django.utils import translation
from django.contrib import messages
import requests


def send_to_telegram(message, apiToken, chatID):
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
    try: response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
    except Exception as e: pass


def index(request):
    teams = Team.objects.all()
    stats = Stats.objects.filter()
    supports = Testimonials.objects.all()
    works = Portfolio.objects.all()
    context = {
        'active': 'index',
        'supports': supports,
        'teams':teams,
        'works':works,
        'stats':stats,
        'lan': get_language()

    }
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        subject = 'Itoutsourcing.uz saytingidan xabar'
        try:
            if name:
                for acount in Telegram.objects.all():
                    send_to_telegram(f"{subject}\nIsm: {name}\nEmail: {email}\nXabar: {message}", acount.apiToken, acount.chatID)
                Xabar.objects.create(User=name, Email=email, Phone=phone, Message=message)
                messages.success(request, "Muvaffaqiyatli yuborildi!")
        except Exception as e:
            return HttpResponse(e)
        return redirect('index')


    return render(request, 'index.html', context)


def portfolio(request, pk):
    works = Portfolio.objects.all()
    work = Portfolio.objects.get(id=pk)


    context = {
        'active': 'portfolio',
        'works': works,
        'work':work,
        'lan': get_language()

    }
    return render(request, 'portfolio-details.html', context)

    
def set_language(request, language):
    for lang, _ in settings.LANGUAGES:
        translation.activate(lang)
        try:
            view = resolve(urlparse(request.META.get("HTTP_REFERER")).path)
        except Resolver404:
            view = None
        if view:
            break
    if view:
        translation.activate(language)
        next_url = reverse(view.url_name, args=view.args, kwargs=view.kwargs)
        response = HttpResponseRedirect(next_url)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    else:
        response = HttpResponseRedirect("/")
    return response