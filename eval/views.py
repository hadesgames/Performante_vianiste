from django.shortcuts import render_to_response

def problems(request, contest_id):
  return render_to_response("problems.html")
  
