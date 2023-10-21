from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.csrf import csrf_exempt
import json
from student.models import Student
from django.views import View
from apps.users.models import  CommonUser
from student.models import *
from student.forms import *
from datetime import datetime

id = CommonUser.get_identity
PARENT = 'teacher/students/'

def apply_leave(request):
    caller = id(request.user.identity) + '/index.html'
    form = LeaveReportStudentForm(request.POST or None)
    student = get_object_or_404(Student, pk=request.user.id)

    context = {
        'caller': caller,
        'form': form,
        'leave_history': LeaveReportStudent.objects.filter(student=student),
        'page_title': 'Apply for leave'
    }

    if request.method == 'POST':
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.student = student
                obj.save()
                messages.success(
                    request, "Application for leave has been submitted for review")
                return redirect(reverse('student_apply_leave'))
            except Exception:
                messages.error(request, "Could not submit")
        else:
            messages.error(request, "Form has errors!")
    return render(request, "student/student_apply_leave.html", context)

def feedback(request):
    caller = id(request.user.identity) + '/index.html'
    form = FeedbackStudentForm(request.POST or None)
    student = get_object_or_404(Student, pk=request.user.id)
    context = {
        'caller': caller,
        'form': form,
        'feedbacks': FeedbackStudent.objects.filter(student=student),
        'page_title': 'Student Feedback'

    }
    if request.method == 'POST':
        if form.is_valid():
            try:
                obj = form.save(commit=False)
                obj.student = student
                obj.save()
                messages.success(
                    request, "Feedback submitted for review")
                return redirect(reverse('student_feedback'))
            except Exception:
                messages.error(request, "Could not Submit!")
        else:
            messages.error(request, "Form has errors!")
    return render(request, "student/student_feedback.html", context)

def notification(request):
    caller = id(request.user.identity) + '/index.html'
    notifications = NotificationStudent.objects.order_by('created_at', 'updated_at')
    context = {
        'caller': caller,
        'notifications': notifications,
        'page_title': "View Notifications"
    }
    return render(request, "student/student_view_notification.html", context)

def view_assignments(request):
    caller = id(request.user.identity) + '/index.html'
    student = get_object_or_404(Student, pk=request.user.id)
    context = {
        'caller': caller,
        'assignments' : student.assignments.all(),
        'page_title': 'View Assignment'
        }

    return render(request, "student/student_view_assignments.html", context)

def view_profile(request):
    caller = id(request.user.identity) + '/index.html'
    student = get_object_or_404(Student, pk=request.user.id)
    form = StudentEditForm(request.POST or None, request.FILES or None,instance=student)
    context = {
        'caller': caller,
        'form': form,
               'page_title': 'View/Edit Profile'
        }
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
                student.save()
                messages.success(request, "Profile Updated!")
                return redirect(reverse('student_view_profile'))
            else:
                messages.error(request, "Invalid Data Provided")
        except Exception as e:
            messages.error(
                request, "Error Occured While Updating Profile " + str(e))

    return render(request, "student/student_view_profile.html", context)

def result(request):
    caller = id(request.user.identity) + '/index.html'
    student = get_object_or_404(Student, pk=request.user.id)
    results = StudentResult.objects.filter(student=student)
    context = {
        'caller': caller,
        'results': results,
        'page_title': "View Results"
    }
    return render(request, "student/student_view_result.html", context)


# @ csrf_exempt
# def student_view_attendance(request):
#     student = get_object_or_404(Student, pk=request.user.id)
#     if request.method != 'POST':
#         course = get_object_or_404(Course, id=student.course.id)
#         context = {
#             'subjects': Subject.objects.filter(course=course),
#             'page_title': 'View Attendance'
#         }
#         return render(request, 'student_template/student_view_attendance.html', context)
#     else:
#         subject_id = request.POST.get('subject')
#         start = request.POST.get('start_date')
#         end = request.POST.get('end_date')
#         try:
#             subject = get_object_or_404(Subject, id=subject_id)
#             start_date = datetime.strptime(start, "%Y-%m-%d")
#             end_date = datetime.strptime(end, "%Y-%m-%d")
#             attendance = Attendance.objects.filter(
#                 date__range=(start_date, end_date), subject=subject)
#             attendance_reports = AttendanceReport.objects.filter(
#                 attendance__in=attendance, student=student)
#             json_data = []
#             for report in attendance_reports:
#                 data = {
#                     "date":  str(report.attendance.date),
#                     "status": report.status
#                 }
#                 json_data.append(data)
#             return JsonResponse(json.dumps(json_data), safe=False)
#         except Exception as e:
#             return None


class StudentAPi(View):
    '''
    TODO: Implement this Generic View to remove all the redudancy
    '''


def student_list(request):
    caller = id(request.user.identity) + '/index.html'
    students = Student.objects.all()
    paginator = Paginator(students, Student.objects.count())
    page = request.GET.get('page')
    paged_students = paginator.get_page(page)

    context = {
        'caller': caller,
        "students": paged_students
    }
    return render(request, PARENT  + "student_list.html", context)

def single_student(request, student_id):
    caller = id(request.user.identity) + '/index.html'
    single_student = get_object_or_404(Student, pk=student_id)
   
    context = {
        'caller': caller,
        "single_student": single_student
    }
   
    return render(request, PARENT + "student_details.html", context)

# def student_regi(request):
#     if request.method == "POST":
#         forms = CreateStudent(request.POST)

#         if forms.is_valid():
#             forms.save()
#         messages.success(request, "Student Registration Successfully!")
#         return redirect("student_list")
#     else:
#         forms = CreateStudent()

#     context = {
#    'caller': caller,
#         "forms": forms
#     }
#     return render(request, PARENT + "registration.html", context)


# def edit_student(request, pk):
#     student_edit = Student.objects.get(id=pk)
#     edit_forms = CreateStudent(instance=student_edit)

#     if request.method == "POST":
#         edit_forms = CreateStudent(request.POST, instance=student_edit)

#         if edit_forms.is_valid():
#             edit_forms.save()
#             messages.success(request, "Edit Student Info Successfully!")
#             return redirect("student_list")

#     context = {
#           'caller': caller,
#         "edit_forms": edit_forms
#     }
#     return render(request, PARENT + "edit_student.html", context)


# def delete_student(request, student_id):
#     student_delete = Student.objects.get(id=student_id)
#     student_delete.delete()
#     messages.success(request, "Delete Student Info Successfully")
#     return redirect("student_list")


# def attendance_count(request):
#     class_name = request.GET.get("class_name", None)
#     if class_name:
#         student_list = Student.objects.filter(
#             class_type__class_short_form=class_name)
#         context = {
# 'caller': caller,"student_list": student_list}
#     else:
#         context = {
# 'caller': caller,}
#     return render(request, PARENT + "attendance_count.html", context)
