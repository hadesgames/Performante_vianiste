from django.core.management import setup_environ
import settings

setup_environ(settings)

from  eval.models import *
  
def do_work(answer):
  # validate that the contest is still running
  team = answer.team
  problem = answer.problem
  contest = problem.contest
  

  if contest.start_time + datetime.timedelta(minutes = constest.duration) < datetime.now() :
    answer.done = True
    answer.save()
    return

  # setup coeficient for the special problem

  if team.special_problem == problem:
    multiplier = 2
  else:
    multiplier = 1

  if problem.solution == answer.solution :
    #good answer
    pass
  else:
    #wrong answer
    pass      

  
  
  

def work():
  while 1:
    answer_list = Answer.objects.filter(done = False)
    for answer in answer_list:
      do_work(answer)
    break



if __name__=="__main__" :
  work()
    
    
