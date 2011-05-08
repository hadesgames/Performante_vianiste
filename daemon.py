from django.core.management import setup_environ
import settings

setup_environ(settings)

from  eval.models import *
mode = "DEBUG"

bonus = [20, 15, 10, 8, 6, 5, 4, 3, 2, 1]
solved_all_bonus = [100, 60, 40, 30, 20, 10]

def do_work(answer):
  # validate that the contest is still running
  # TO DO: bonus for when a team completes all the problems
  team = answer.team
  problem = answer.problem
  contest = problem.contest
  
  if contest.time_passed_minutes() >= contest.duration :
    answer.status = 3
    answer.save()
    return

  #check if the the problem has already been answered by this team

  if team.answer_set.filter(status = 2, problem = problem).exists() :
    answer.status = 3
    answer.save()
    return 

  if problem.solution == answer.solution :
    #good answer
    answer.status = 2
    
    points_gained = problem.score()
    try:
      points_gained += bonus[problem.correct]
    except IndexError:
      pass

    team.solved+=1
    if team.solved == contest.problem_set.count():
      try:
        points_gained += solved_all_bonus[contest.fully_solved]
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
    problem.value += problem.can_score_change() and -2
    problem.save()
    
  if problem == team.special_problem:
    points_gained *= 2
    team.special_score += points_gained
    
  team.score += points_gained
  team.save()
  answer.save()

def work():
  while 1:
    answer_list = Answer.objects.filter(status = 0)
    for answer in answer_list:
      do_work(answer)
    break



if __name__=="__main__" :
  work()
    
    
