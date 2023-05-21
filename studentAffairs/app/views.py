from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Student


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
  template = loader.get_template('view.html')
  return HttpResponse(template.render())

def addStudent(request):
  template = loader.get_template('add_student.html')
  return HttpResponse(template.render())

def editStudent(request):
  template = loader.get_template('edit_student.html')
  return HttpResponse(template.render())

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

  name = request.post.get('student-name')
  id = request.post.get('student-id')
  email = request.post.get('email')
  phone = request.post.get('phone')
  # name = request.post.get('name')
  # name = request.post.get('name')

  toSave = Student(name = name, id = id ,email =email, phone = phone)
  toSave.save()

  return HttpResponseRedirect(reverse('home/student_screen'))
