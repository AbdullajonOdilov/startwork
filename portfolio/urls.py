from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path("set_language/<str:language>/", views.set_language, name="set-language"),
    path('portfolio/<int:pk>/', views.portfolio, name='portfolio'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)