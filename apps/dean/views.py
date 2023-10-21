import json
from django.http import HttpRequest as requests
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import (HttpResponse, HttpResponseRedirect, get_object_or_404, redirect, render)
from django.templatetags.static import static
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from student.models import FeedbackStudent, Student, NotificationStudent
from django.core.paginator import Paginator
from apps.users.models import  CommonUser
from teacher.models import Teacher


id = CommonUser.get_identity
PARENT = 'dean/teachers/'

@csrf_exempt
def student_feedback_message(request):

    caller = id(request.user.identity) + '/index.html'
    if request.method != 'POST':
        feedbacks = FeedbackStudent.objects.all()
        context = {
            'caller': caller,
            'feedbacks': feedbacks,
            'page_title': 'Student Feedback Messages'
        }
        return render(request, 'dean/student_feedback_template.html', context)
    else:
        feedback_id = request.POST.get('id')
        try:
            feedback = get_object_or_404(FeedbackStudent, id=feedback_id)
            reply = request.POST.get('reply')
            feedback.reply = reply
            feedback.save()
            return HttpResponse(True)
        except Exception as e:
            return HttpResponse(False)

def notify_student(request):
    caller = id(request.user.identity) + '/index.html'
    student = Student.objects.all()
    context = {
        'caller': caller,
        'page_title': "Send Notifications To Students",
        'students': student
    }
    return render(request, "dean/student_notification.html", context)

@csrf_exempt
def send_student_notification(request):
    message = request.POST.get('message')
    notification = NotificationStudent(message=message)
    notification.save()
    return HttpResponse("True")


def teacher_list(request):
    caller = id(request.user.identity) + '/index.html'
    teachers = Teacher.objects.all()

    paginator = Paginator(teachers, Teacher.objects.count())
    page = request.GET.get('page')
    paged_teachers = paginator.get_page(page)
    context = {
        'caller': caller,
        "teachers": paged_teachers
    }
    return render(request, PARENT + "teacher_list.html", context)


# TODO: implement these methods
def assesss_teacher_list(): pass
