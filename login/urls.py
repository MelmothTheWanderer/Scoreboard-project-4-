from . import views
from django.urls import path 

urlpatterns = [
    path('', views.ScoreList.as_view(),name='score')
]