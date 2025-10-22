from django.urls import path
from . import views

urlpatterns = [
    path("soma/<int:a>/<int:b>", views.soma, name="soma_polls"),
    path("home/", views.home, name="pools_home"),
]