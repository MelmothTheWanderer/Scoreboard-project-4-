from django.shortcuts import render, redirect
from django.views import generic
from .models import Score
from login.forms import ScoreForm

# Create your views here.
class ScoreList(generic.ListView):
    queryset = Score.objects.all()
    template_name='login/index.html'

    def get(self, request):
        if request.user.is_authenticated:
            scores = Score.objects.filter(user=request.user)
            form = ScoreForm()
            
            return render(request, 'login/index.html', {
                'scores': scores,
                'form' : form,
            }
            )
        else:
            return redirect('account_login')