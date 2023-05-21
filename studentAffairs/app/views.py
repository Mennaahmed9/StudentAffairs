from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from datetime import date
from app.models import Student

from .models import Student

students = [
    {
        'name': 'Shefa',
        'id': 1,
        'email': 'emil@example.com',
        'phone': 1234567890,
        'gender': 'Female',
        'status': 'Active',
        'level': 1,
        'department': 'IT',
        'gpa': 3.5,
        'nationalid': 12345,
        'nationality': 'USA',
        'birthdate': date.today()
    },
    {
        'name': 'John',
        'id': 2,
        'email': 'john@example.com',
        'phone': 9876543210,
        'gender': 'Male',
        'status': 'Inactive',
        'level': 2,
        'department': 'CS',
        'gpa': 3.2,
        'nationalid': 54321,
        'nationality': 'UK',
        'birthdate': date(1995, 5, 10)
    },
]


def app(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())


def studentScreen(request):
    template = loader.get_template('student_screen.html')
    return HttpResponse(template.render())


def help(request):
    template = loader.get_template('help.html')
    return HttpResponse(template.render())


def search(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())


def view(request):
    students = Student.objects.all()
    return render(request, 'view.html', {'students': students})


def addStudent(request):
    template = loader.get_template('add_student.html')
    return HttpResponse(template.render())


def editStudent(request, id):
    student = {
        'student': Student.objects.get(id=id)}
    return render(request, 'edit_student.html', student)


def departmentAssignment(request):
    template = loader.get_template('department_assignment.html')
    return HttpResponse(template.render())


def editAdmin(request):
    template = loader.get_template('edit_admin.html')
    return HttpResponse(template.render())


def signin(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render())


def fAddStudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        student_id = request.POST['id']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        status = request.POST['status']
        level = request.POST['level']
        department = request.POST['department']
        gpa = request.POST['gpa']
        nationalid = request.POST['nationalid']
        nationality = request.POST['nationality']
        birthdate = request.POST['birthdate']

        student = Student(
            name=name,
            id=student_id,
            email=email,
            phone=phone,
            gender=gender,
            status=status,
            level=level,
            department=department,
            gpa=gpa,
            nationalid=nationalid,
            nationality=nationality,
            birthdate=birthdate
        )
        student.save()
        return HttpResponseRedirect(reverse('studentScreen'))
