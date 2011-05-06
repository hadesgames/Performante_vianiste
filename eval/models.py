from django.db import models
import datetime

# Create your models here.

class Contest(models.Model):
  
  start_time = models.DateTimeField()
  duration = models.IntegerField()
  fully_solved = models.IntegerField(default = 0)
  def time_passed(self):
    return datetime.datetime.now() - self.start_time
  

class Problem(models.Model):

  solution = models.CharField(max_length = 10)
  
  value = models.IntegerField(default = 20)
  corect = models.IntegerField(default = 0)
  
  contest = models.ForeignKey(Contest)
    

  def score_can_change(self):
    return ( self.corect == 0 and
             self.contest.duration - self.contest.time_passed().minutes > 20 )

  def score(self):
    extra_points = self.can_score_change() and self.contest.time_passed().minutes or 0  
    return self.value + extra_points
    
    

class Team(models.Model):

  name = models.CharField(max_length = 40)
  score = models.IntegerField(default = 120 )
  special_score = models.IntegerField(default = 0)
  special_problem = models.ForeignKey(Problem)



class Answer(models.Model):

  time = models.DateTimeField()
  team = models.ForeignKey(Team)
  status = models.IntegerField(default = 0)
  # 0 - Not evaluated
  # 1 - Evaluated but wrong
  # 2 - Evaluated and correct
  # 3 - Evaluated but ignored
  problem = models.ForeignKey(Problem)
  solution = models.CharField(max_length = 10)
  
  
  
  




  
  
