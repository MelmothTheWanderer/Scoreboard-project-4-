from django.shortcuts import render
from django.views import generic
from .models import Score

# Create your views here.
class ScoreList(generic.ListView):
    model = Score