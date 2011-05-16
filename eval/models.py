from django.db import models
import datetime

# Create your models here.

class Contest(models.Model):
  
  start_time = models.DateTimeField()
  duration = models.IntegerField()
  fully_solved = models.IntegerField(default = 0)
  
  def __unicode__(self):
    return "%s" % self.pk
    
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
  
  contest = models.ForeignKey(Contest, default = 1)
  
  def __unicode__(self):
    return self.name 

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
  contest = models.ForeignKey(Contest, default = 1)
  solved = models.IntegerField(default = 0) 
  score = models.IntegerField(default = 120 )
  special_score = models.IntegerField(default = 0)
  #This is so wrong: 
  special_problem = models.ForeignKey(Problem, blank = True, null = True)
  
  def __unicode__(self):
    return "%s" % self.name


class Answer(models.Model):

  time = models.DateTimeField(default = datetime.datetime.now())
  team = models.ForeignKey(Team)
  status = models.IntegerField(default = 0)
  # 0 - Not evaluated
  # 1 - Evaluated but wrong
  # 2 - Evaluated and correct
  # 3 - Evaluated but ignored
  problem = models.ForeignKey(Problem)
  solution = models.CharField(max_length = 10)
  
  def __unicode__(self):
    return "On %s by %s" % (self.problem.name, self.team.name)
  
  
  




  
  
