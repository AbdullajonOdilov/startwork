from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Projects, Proposal
from django.contrib import messages


def index(request):
    projects = Projects.objects.filter(start_date__isnull=True)
    project_types = projects.values_list('type', flat=True).distinct()
    context = {
        "projects": projects,
        "active": "work-1",
        "project_types": project_types,
    }
    return render(request, 'index.html', context=context)

def proposal(request, project_id):
    if request.user and request.user.is_authenticated and request.method == 'POST':
        message = request.POST.get('message')
        Proposal.objects.create(project=Projects.objects.get(id=project_id), user=request.user, message=message)
        messages.success(request, f'Amal muvaffaqiyatli bajarildi.')
        response = redirect('work:index')
        return response
    return redirect("work:index")

def project_details_view(request, project_id):
    project = get_object_or_404(Projects, id=project_id)
    context = {
        'project': project,
        "active": "work-1",

    }
    return render(request, 'loyiha_detail.html', context)

def proposal_view(request):
    proposals = Proposal.objects.filter(user=request.user)
    context = {
        "proposals": proposals,
        "active": "work-2",
    }
    return render(request, 'proposal_view.html', context=context)

def logout_user(request):
    logout(request)
    response = redirect('/')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response
