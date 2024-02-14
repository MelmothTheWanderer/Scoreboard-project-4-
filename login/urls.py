from . import views
from django.urls import path 

urlpatterns = [
    path('', views.ScoreList.as_view(),name='score'),
    path('add_score', views.add_score, name='add'),
]