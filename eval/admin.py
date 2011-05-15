from django.contrib import admin
from models import *

class ContestAdmin(admin.ModelAdmin):
  fields = ("start_time","duration")
  
  
admin.site.register(Contest, ContestAdmin)

class ProblemAdmin(admin.ModelAdmin):
  fields = ("solution", "name", "contest")


admin.site.register(Problem, ProblemAdmin)

class TeamAdmin(admin.ModelAdmin):
  fields = ("name","contest")
        
        
admin.site.register(Team, TeamAdmin)

class AnswerAdmin(admin.ModelAdmin):
  fields = ("problem", "team", "solution")
  

admin.site.register(Answer, AnswerAdmin)