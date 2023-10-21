from django.urls import path
from student.views import *

urlpatterns = [
    path('allstudents/', student_list, name='student_list'),
    path('<int:student_id>/', single_student, name='single_student'),
    # path('registration/', student_regi, name='student_regi'),
    # path('edit/<int:pk>', edit_student, name='edit_student'),
    # path('delete/<int:student_id>', delete_student, name='delete_student'),
    # path('attendance/count', attendance_count, name='attendance_count'),
    # path("home/", home, name='home'),
    # path("view/attendance/", view_attendance,
    #      name='view_attendance'),
    path("apply/leave/", apply_leave, name='student_apply_leave'),
    path("feedback/", feedback, name='student_feedback'),
    path("view/profile/", view_profile, name='student_view_profile'),
    path("view/assignments/", view_assignments, name='student_view_assignments'),
    # path("fcmtoken/", fcmtoken,
    #      name='fcmtoken'),
    path("view/notification/", notification, name="student_view_notification"),
    path('view/result/', result,  name='student_view_result'),
    
]
