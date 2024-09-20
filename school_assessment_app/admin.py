from django.contrib import admin
from .models import School, Class, Student, Subject, AssessmentAreas, Answers, Awards, Summary

admin.site.register(School)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(AssessmentAreas)
admin.site.register(Answers)
admin.site.register(Awards)
admin.site.register(Summary)
