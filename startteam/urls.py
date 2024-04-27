from django.urls import path
from .views import *

app_name = 'work'

urlpatterns = [
    path('', index, name='index'),
    path('logout_user/', logout_user, name='logout_user'),
    path('work-detail/<int:project_id>/', project_details_view, name='project_details_view'),
    path('proposal/<int:project_id>/', proposal, name='proposal'),
    path('proposal_view/', proposal_view, name='proposal_view'),
    path('jamoalar/', jamoalar, name='jamoalar'),
    path('tasks/', tasks, name='tasks'),
    path('team_details_view/<int:team_id>/', team_details_view, name='team_details_view'),
    path('task_details_view/<int:task_id>/', task_details_view, name='task_details_view'),
    path('tranzaksiya/', tranzaksiya, name='tranzaksiya'),
    
]