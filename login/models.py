from django.db import models
'''
In the line of code below , we are importing the built-in User model that 
comes with Django. 
'''
from django.contrib.auth.models import User
# Create your models here.

class Score(models.Model):
        user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
        name=models.CharField(max_length=50)
        score_value = models.IntegerField()


