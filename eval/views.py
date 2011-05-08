from django.shortcuts import render_to_response
import models

def problems(request, contest_id):
  return render_to_response("problems.html",{"api_address" : "/sever/api/problems/1",
      "time_left": models.Contest.objects.get(pk = contest_id).duration * 60 - models.Contest.objects.get(pk = contest_id).time_passed()})

def teams(request, contest_id):
  return render_to_response("teams.html", {"api_address" : "/sever/api/teams/1"})

def table(request, contest_id):
  return render_to_response("table.html",{"api_address" : "/sever/api/table/1"})
