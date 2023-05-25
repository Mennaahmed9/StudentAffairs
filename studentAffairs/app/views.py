from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect
from django.template import RequestContext
# from django.views.decorators.csrf import csrf_protect
from datetime import date
from .models import Student
from .models import Admin

from .models import Student

from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse


def app(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def profile(request):
    admin = Admin.objects.first()
    return render(request, 'profile.html', {'admin': admin})


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

@csrf_exempt
def updateStudentStatus(request, student_id):
    if request.method == 'POST':
        student = Student.objects.get(id=student_id)
        payload = json.loads(request.body)
        new_status = payload.get('status')

        student.status = new_status
        student.save()

        return JsonResponse({'message': 'Status updated successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'})


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
    admin = Admin.objects.first()
    return render(request, 'edit_admin.html', {'admin': admin})


@csrf_exempt
def saveAdmin(request):
    admin = Admin.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        admin.name = name
        admin.email = email
        admin.phone = phone
        admin.save()
        return HttpResponseRedirect(reverse('profilepage'))
    else:
        return HttpResponseRedirect(reverse('editAdminpage'))


def signin(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render())


@csrf_exempt
def authenticate(request):
    try:
        if request.method == 'POST':
            admin = Admin.objects.first()
            email = request.POST.get('email')
            password = request.POST.get('pw')
            if email == admin.email and password == admin.password:
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponseRedirect(reverse('signinpage'))
    except Exception as e:
        return JsonResponse({'error': str(e)})


@csrf_exempt
def fAddStudent(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            student_id = request.POST.get('id')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            gender = request.POST.get('gender')
            status = request.POST.get('status')
            level = request.POST.get('level')
            department = request.POST.get('department')
            gpa = request.POST.get('gpa')
            nationalid = request.POST.get('nationalid')
            nationality = request.POST.get('nationality')
            birthdate = request.POST.get('birthdate')
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
            print(student)
            student.save()
            return HttpResponseRedirect(reverse('viewpage'))
    except Exception as e:
        return JsonResponse({'error': str(e)})
