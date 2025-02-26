from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name = "portfolio"
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path("register/", views.signup, name='register'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)