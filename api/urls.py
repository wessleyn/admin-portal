from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

# API endpoints
urlpatterns = format_suffix_patterns(
    [
        path('all-students-list/', views.StudentList.as_view(), name='all-students-list'),
        path('all-teachers-list/', views.TeacherList.as_view(), name='all-teachers-list'),
        path('all-parents-list/', views.ParentList.as_view(), name='all-parents-list'),
        path('all-classrooms-list/', views.ClassRoomList.as_view(), name='all-classrooms-list'),
        path('all-subjectslist/', views.SubjectList.as_view(), name='all-subjects-list'),
        path('all-bookslist/', views.BookList.as_view(), name='all-books-list'),
        path('all-examslist/', views.ExamList.as_view(), name='all-exams-list'),
        path('all-gradelist/', views.GradeList.as_view(), name='all-grade-list'),
        path('all-vehiclelist/', views.VehicleList.as_view(), name='all-vehicle-list'),
        path('all-hostellist/', views.HostelList.as_view(), name='all-hostel-list'),
        path('all-classtimetableslist/', views.ClassTimeTableList.as_view(), name='all-classtimetable-list'),
        path('all-attendencieslist/<int:pk>', views.AttendencyDetail.as_view(), name='all-attendencies-list'),
    ]
)
