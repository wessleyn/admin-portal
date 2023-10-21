from django.urls import path
from dean.views import *

urlpatterns = [

    # Adminstration of Staff
    path('dean_all_teachers/', teacher_list, name='dean_all_teachers'),

    path(
        "student/view/feedback/", 
        student_feedback_message,
        name="student_feedback_message",
    ),

    path(
        "notify_students", 
        notify_student,
         name='notify_student'
    ),

    path(
        "send_student_notification/", 
        send_student_notification,
        name='send_student_notification'
    ),

]
