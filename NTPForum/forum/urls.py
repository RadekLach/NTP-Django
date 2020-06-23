from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name="homeView"),
    path('thread/', views.threadView, name="threadView"),
    path('thread/<int:idx>', views.threadView, name="threadView"),
    path('createthread/', views.createThreadView, name="createThreadView"),
]
