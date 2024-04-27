from django.urls import path
from .views import *

app_name = 'work'

urlpatterns = [
    path('', index, name='index'),
    path('logout_user/', logout_user, name='logout_user'),
    path('work-detail/<int:project_id>/', project_details_view, name='project_details_view'),
]