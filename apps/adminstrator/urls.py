from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('notice/', notice, name='notice'),
    path('message/', message, name='message'),
    path('settings/', settings, name='settings'),
    
    path('allstudents/', allstudents, name='all_students'),
    path('allteachers/', allteachers, name='all_teachers'),
    path('allparents/', allparents, name='all_parents'),
    path('allclassrooms/', allclassrooms, name='all_classrooms'),
    path('allsubjects/', allsubjects, name='all_subjects'),
    path('allbooks/', allbooks, name='all_books'),
    path('allexams/', allexams, name='all_exams'),
    path('alltransport/', alltransport, name='all_transport'),
    path('allhostel/', allhostel, name='hostel'),
    path('allclasstimetable/', allclasstimetable, name='allclasstimetable'),
    path('allgrades/', allgrades, name='allgrades'),
    path('allattendances/', allattendances, name='all_attendances'),
] 
