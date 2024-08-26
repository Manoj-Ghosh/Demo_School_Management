

# Create your views here.

from django.shortcuts import render
from .models import Student, Teacher, Class


def index(request):
    return render(request, 'index.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})


def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})
