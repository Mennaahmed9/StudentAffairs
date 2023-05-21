from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('signin/', views.signin, name='signinpage'),
    path('home/', views.home, name='homepage'),
    path('home/profile', views.profile, name='profilepage'),
    path('home/student_screen', views.studentScreen, name='studentScreen'),
    path('home/help', views.help, name='helppage'),
    path('home/student_screen/search', views.search, name='searchpage'),
    path('home/student_screen/view', views.view, name='viewpage'),
    path('home/student_screen/add_student', views.addStudent, name='addStudentpage'),
    path('home/student_screen/edit_student', views.editStudent, name='editpage'),
    path('home/student_screen/edit_student', views.editStudent, name='editpage'),
    path('home/student_screen/search/department_assignment', views.departmentAssignment, name='departmentpage'),
    path('home/profile/edit_admin', views.editAdmin, name='editAdminpage'),
    path('home/student_screen', views.fAddStudent, name='')
    

]