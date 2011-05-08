from django.shortcuts import render_to_response
import models


def problems(request, contest_id):
  return render_to_response("problems.html",{"api_address" : "/sever/api/problems/%s" % contest_id,
      "time_left": models.Contest.objects.get(pk = contest_id).time_remaining()})

def teams(request, contest_id):
  return render_to_response("teams.html", {"api_address" : "/sever/api/teams/%s" % contest_id,
      "time_left": models.Contest.objects.get(pk = contest_id).time_remaining()})

def table(request, contest_id):
  return render_to_response("table.html",{"api_address" : "/sever/api/table/%s" % contest_id,
      "time_left": models.Contest.objects.get(pk = contest_id).time_remaining()})
