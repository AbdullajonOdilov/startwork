from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('logout_user/', logout_user, name='logout_user'),
]