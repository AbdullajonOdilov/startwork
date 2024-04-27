from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Projects


def index(request):
    projects = Projects.objects.filter(start_date__isnull=True)
    project_types = projects.values_list('type', flat=True).distinct()
    context = {
        "projects": projects,
        "project_types": project_types,
    }
    return render(request, 'index.html', context=context)

def logout_user(request):
    logout(request)
    response = redirect('/')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response
