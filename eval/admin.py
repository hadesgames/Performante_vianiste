from django.contrib import admin
from models import *

class ContestAdmin(admin.ModelAdmin):
  fields = ("start_time", "duration")
  
  
admin.site.register(Contest, ContestAdmin)

class ProblemAdmin(admin.ModelAdmin):
  fields = ("solution", "name", "contest")


admin.site.register(Problem, ProblemAdmin)

class TeamAdmin(admin.ModelAdmin):
  fields = ("name", "contest", "special_problem")
  
  def get_readonly_fields(self, request, obj=None):
    if obj is None:
        return ()
    if obj.special_problem is not None:
        return ("special_problem",)
    return ()
        
        
admin.site.register(Team, TeamAdmin)

class AnswerAdmin(admin.ModelAdmin):
  fields = ("team", "problem", "solution")
  

admin.site.register(Answer, AnswerAdmin)
