from django.shortcuts import render_to_response

def problems(request, contest_id):
  return render_to_response("problems.html",{"api_address" : "/sever/api/problems/1"})

def teams(request, contest_id):
  return render_to_response("teams.html", {"api_address" : "/sever/api/teams/1"})

def table(request, contest_id):
  return render_to_response("table.html",{"api_address" : "/sever/api/table/1"})
