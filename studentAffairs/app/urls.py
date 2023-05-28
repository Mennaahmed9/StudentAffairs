from django.urls import path
from . import views

urlpatterns = [
    path('', views.app, name='app'),
    path('signin/', views.signin, name='signinpage'),
    path('signin/authenticate', views.authenticate, name='authenticate'),
    path('home/', views.home, name='homepage'),
    path('home/profile', views.profile, name='profilepage'),
    path('home/student_screen', views.studentScreen, name='studentScreen'),
    path('home/help', views.help, name='helppage'),
   # path('home/student_screen/search/<string:search_name>', views.search, name='searchpage'),
    path('home/student_screen/add', views.fAddStudent, name=''),
    path('home/student_screen/view', views.view, name='viewpage'),
    path('home/student_screen/add_student',
         views.addStudent, name='addStudentpage'),
    path('home/student_screen/edit_student/<int:id>',
         views.editStudent, name='editpage'),
    path('home/student_screen/search/department_assignment',
         views.departmentAssignment, name='departmentpage'),
    path('home/profile/edit_admin', views.editAdmin, name='editAdminpage'),
    path('home/profile/save_admin', views.saveAdmin, name=''),
    path('update_student_status/<int:student_id>/', views.updateStudentStatus, name='updateStudentStatus'),
    path('update_student_info/<int:student_id>/', views.updateStudentInfo, name='updateStudentInfo'),
    path('delete_student/<int:student_id>/', views.deleteStudent, name='deleteStudent'),
]
