from django.db import models

# Create your models here.

class Contest(models.Model):
  
  start_time = models.DateTimeField()
  duration = models.IntegerField()

class Problem(models.Model):

  solution = models.CharField(max_length = 10)
  
  value = models.IntegerField(default = 20)
  wrong = models.IntegerField(default = 0)
  corect = models.IntegerField(default = 0)
  
  contest = models.ForeignKey(Contest)

class Team(models.Model):

  name = models.CharField(max_length=40)
  score = models.IntegerField()
  special_problem = models.ForeignKey(Problem)

class Answer(models.Model):

  time = models.DateTimeField()
  team = models.ForeignKey(Team)
  done = models.BooleanField(default = False)
  problem = models.ForeignKey(Problem)
  solution = models.CharField(max_length = 10)
  
  




  
  
