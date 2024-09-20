from django.shortcuts import render
from django.http import JsonResponse
from .models import School, Class, Student, Subject,AssessmentAreas,Answers,Awards,Summary

def school_data_view(request):
    #fetch data from the modeks
    schools=School.objects.all()
    classs=Class.objects.all()
    students=Student.objects.all()
    subjects=Subject.objects.all()
    assessmentareas=AssessmentAreas.objects.all()
    answers=Answers.objects.all()
    awards=Awards.objects.all()
    summarys=Summary.objects.all()
    
    context={
        'schools':schools,
        'classs' :classs,
        'students':students,
        'subjects':subjects,
        'assessmentareas':assessmentareas,
        'answers':answers,
        'awards':awards,
        'summarys':summarys,
    }
    return render(request, 'index.html',context)
def Award(request):
    return render(request,'awards.html')
def about(request):
    return render(request,'about.html')


def student_data(request):
    # Load your student data from a .txt file or database
    students = [
        {"id": 1, "fullName": "John Doe", "class": "Class 10", "award": "Best Student"},
        {"id": 2, "fullName": "Jane Smith", "class": "Class 12", "award": "Top Scorer"},
        # Add more students
    ]
    return JsonResponse(students, safe=False)

