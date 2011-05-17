# Create your views here.
from django.http import HttpResponse
import json
import models

# All this codes makes the important data from models json encodable
def _get_data_functions(obj, fields):
  result={}
  for field in fields:
    result[field] = getattr(obj, field, lambda : None) ()
  return result

def _get_data(obj, fields):
  result={}
  for field in fields:
    result[field] = getattr(obj, field, None)
  return result

def _get_object_list(obj_list, fields=[], function_fields=[]):
  output=[]
  
  for obj in obj_list:
    data={}
    data.update(_get_data(obj, fields))
    data.update(_get_data_functions(obj, function_fields))
    output.append(data)
    
  return output
    
def problems(request, contest_id):
  function_fields = ["score", "score_can_change"]
  fields = ["name", "correct"]
  problem_list = models.Contest.objects.get(pk = contest_id).problem_set.all()
  
  return HttpResponse(json.dumps(_get_object_list(problem_list, fields, function_fields)))

def teams(request, contest_id):
  fields = ["name", "score"]
  function_fields = []
  team_list = models.Contest.objects.get(pk = contest_id).team_set.all()

  return HttpResponse(json.dumps(_get_object_list(team_list, fields, function_fields)))

def table(request, contest_id):
  #This is probably very inefficient.
  problem_list = models.Contest.objects.get(pk = contest_id).problem_set.all()
  
  team_list = models.Contest.objects.get(pk = contest_id).team_set.all()
  output=[]
  for team in team_list:
    row={"name" : team.name, "score_list":[], "special_problem" : -1}
    if team.special_problem is not None:
      row["special_problem"] = team.special_problem.pk; 
    for problem in problem_list:
      element={}
      element["id"] = problem.id;
      #Inefficient part : 
      element["wrong_tries"] = models.Answer.objects.filter(team = team, problem = problem, status = 1).count()
      element["solved"] = models.Answer.objects.filter(team = team, problem = problem, status = 2).count()
      row["score_list"].append(element);
    output.append(row)

  return HttpResponse(json.dumps(output))
