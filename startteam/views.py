from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Projects


def index(request):
    projects = Projects.objects.filter(start_date__isnull=True)
    project_types = projects.values_list('type', flat=True).distinct()
    context = {
        "projects": projects,
        "active": "work-1",
        "project_types": project_types,
    }
    return render(request, 'index.html', context=context)


def project_details_view(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    context = {
        'project': project,
    }
    return render(request, 'loyiha_detail.html', context)

def logout_user(request):
    logout(request)
    response = redirect('/')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response
