from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
import models
import daemon

def problems(request, contest_id):
  return render_to_response("problems.html",
      {
        "api_address" : reverse("eval.api.problems",args=(contest_id,)),
        "time_left": models.Contest.objects.get(pk = contest_id).time_remaining(),
        "bonus_points" : daemon.bonus
      }, context_instance = RequestContext(request))

def teams(request, contest_id):
  return render_to_response("teams.html", 
      {
        "api_address" : reverse("eval.api.teams",args = (contest_id,)),
        "time_left": models.Contest.objects.get(pk = contest_id).time_remaining()
      }, context_instance = RequestContext(request) )

def table(request, contest_id):
  return render_to_response("table.html",
      {
        "api_address" : reverse("eval.api.table",args = (contest_id,)),
        "time_left": models.Contest.objects.get(pk = contest_id).time_remaining()
      }, context_instance = RequestContext(request))
