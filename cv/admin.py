from django.contrib import admin
from .models import CV, Skill, Education, Experience, Project

admin.site.register(CV)
admin.site.register(Skill)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
