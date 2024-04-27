from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Projects, Proposal, Team, Task, Tranzaksiyalar
from django.contrib import messages
from django.db.models import Q



def index(request):
    projects = Projects.objects.filter(start_date__isnull=True).order_by('-date')
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
    proposals = Proposal.objects.filter(user=request.user).order_by('-date')
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

def jamoalar(request):
    teams = Team.objects.filter(Q(team_lead=request.user) | Q(workers_id=request.user)).order_by('-date')
    print(teams)
    context = {
        "teams": teams,
        "active": "work-3",
    }
    return render(request, 'jamoalar.html', context=context)

def team_details_view(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    context = {
        'team': team,
        "active": "work-3",

    }
    return render(request, 'team_detail.html', context)


def tasks(request):
    tasks = Task.objects.filter(user__id=request.user.id).order_by('-start_date')
    print(tasks)
    context = {
        "tasks": tasks,
        "active": "work-4",
    }
    return render(request, 'tasks.html', context=context)

def task_details_view(request, task_id):
    if request.user and request.user.is_authenticated and request.method == 'POST':
        selected_progress = request.POST.get('progress')
        t = Task.objects.get(id=task_id)
        t.progress = selected_progress
        t.save()
        messages.success(request, f'Amal muvaffaqiyatli bajarildi.')
        return redirect('work:tasks')

    task = get_object_or_404(Task, id=task_id)
    progress_choices = Task()._meta.get_field('progress').choices 
    context = {
        'task': task,
        "active": "work-4",
        "progress_choices": progress_choices,

    }
    return render(request, 'task_detail.html', context)


def tranzaksiya(request):
    tranz = Tranzaksiyalar.objects.filter(user__id=request.user.id).order_by('-date')
    context = {
        "tranz": tranz,
        "active": "work-6",
    }
    return render(request, 'tranzaksiya.html', context=context)