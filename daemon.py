import time
from django.core.management import setup_environ
from django.core.exceptions import ObjectDoesNotExist
import settings

setup_environ(settings)

from  eval.models import *
mode = "DEBUG"

bonus = [20, 15, 10, 8, 6, 5, 4, 3, 2, 1]
solved_all_bonus = [100, 60, 40, 30, 20, 10]

def do_work(answer):
  team = answer.team
  problem = answer.problem
  contest = problem.contest
  
  if contest.time_passed_minutes() >= contest.duration + 5 :
    answer.status = 3
    answer.save()
    return

  #check if the the problem has already been answered by this team

  if team.answer_set.filter(status = 2, problem = problem).exists() :
    answer.status = 3
    answer.save()
    return 
  extra_points = 0;
  if problem.solution == answer.solution :
    #good answer
    answer.status = 2
    
    points_gained = problem.score()
    try:
      points_gained += bonus[problem.correct]
    except IndexError:
      pass
      
    team.solved += 1
    
    if team.solved == contest.problem_set.count():
      try:
        extra_points = solved_all_bonus[contest.fully_solved]
      except IndexError:
        pass
      contest.fully_solved += 1
      contest.save()
    # modify the problem
    if problem.correct == 0:
      problem.time_solved = contest.time_passed_minutes()
    problem.correct += 1
    problem.save()
  else:
    #wrong answer
    answer.status = 1
    
    points_gained = -10
    problem.value += problem.score_can_change() and 2
    problem.save()
  if team.special_problem is None:
    if contest.time_passed_minutes() >= 10:
      team.special_problem = contest.problem_set.order_by("pk")[0]
  if problem == team.special_problem:
    points_gained *= 2
    team.special_score += points_gained
    
  team.score += points_gained + extra_points
  team.save()
  answer.save()

def work():
  while 1:
    answer_list = Answer.objects.filter(status = 0)
    for answer in answer_list:
      do_work(answer)
    time.sleep(3)

if __name__=="__main__" :
  work()    
