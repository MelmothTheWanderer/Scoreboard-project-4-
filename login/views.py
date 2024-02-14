from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Score
from login.forms import ScoreForm
from django.http import HttpResponseRedirect

# Create your views here.
def index (request): 
    if request.user.is_authenticated:

        context = {}
        form = ScoreForm()
        scores = Score.objects.filter(user=request.user)
        context ['scores'] = scores
        context ['title'] = 'Home'

        if request.method == 'POST':
            if 'save' in request.POST:
                form= ScoreForm(request.POST)
                if form.is_valid():
                    score = form.save(commit=False)
                    score.user = request.user
                    score.save()
            elif 'delete' in request.POST:
                pk = request.POST.get('delete')
                score = Score.objects.get(id=pk)
                score.delete()
            elif 'edit' in request.POST:
                pk = request.POST.get('edit')
                score = Score.objects.get(id=pk)
                form = ScoreForm(instance=score)
        context['form'] = form 
        
        return render(request, 'login/index.html', context ) 
    else:
        return redirect('account_login')

