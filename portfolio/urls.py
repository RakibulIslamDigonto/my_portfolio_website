from django.urls import path
from .import views
from django.urls import reverse

app_name = 'portfolio'

urlpatterns = [
    path('', views.fontend, name='fontend'),
]
