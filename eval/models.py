from django.db import models
import datetime

# Create your models here.

class Contest(models.Model):
  
  start_time = models.DateTimeField()
  duration = models.IntegerField()
  fully_solved = models.IntegerField(default = 0)
  def time_passed(self):
    return (datetime.datetime.now() - self.start_time).seconds
  def time_passed_minutes(self):
    return self.time_passed() / 60
  def time_remaining(self):
    return self.duration * 60 - self.time_passed();
  

class Problem(models.Model):

  solution = models.CharField(max_length = 10)
  name = models.CharField(max_length = 30)
  value = models.IntegerField(default = 20)
  correct = models.IntegerField(default = 0)
  # the minute in which the problem  was first solved
  time_solved = models.IntegerField(default = 0)
  
  contest = models.ForeignKey(Contest)
    

  def score_can_change(self):
    return ( self.correct == 0 and
             self.contest.duration - self.contest.time_passed_minutes() > 20 )

  def score(self):
    time_points = (self.time_solved or 
                  (self.score_can_change() and self.contest.time_passed_minutes()) or
                  (self.correct == 0 and self.contest.duration - 20 ))

    return self.value + time_points
    
    

class Team(models.Model):

  name = models.CharField(max_length = 40)
  contest = models.ForeignKey(Contest)
  solved = models.IntegerFielld(default = 0) 
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
  
  
  
  




  
  
