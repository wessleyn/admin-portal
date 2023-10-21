from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_list_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpRequest
from django.db.models import Sum
from django.conf import settings

sep = settings.DIR_SEP
app = 'admin'

@require_GET
def home(request) -> HttpResponse:
    context = {
        'students': ContentType.objects.get(app_label='student', model='student').get_all_objects_for_this_type().__len__(),
        'f_students': ContentType.objects.get(app_label='student', model='student').get_all_objects_for_this_type().filter(
            gender='F'
        ).count(),
        'm_students': ContentType.objects.get(app_label='student', model='student').get_all_objects_for_this_type().filter(
            gender='M'
        ).count(),
        'teachers': ContentType.objects.get(app_label='teacher', model='teacher').get_all_objects_for_this_type().__len__(),
        'parents': ContentType.objects.get(app_label='student', model='parent').get_all_objects_for_this_type().__len__(),
        'funds': ContentType.objects.get(app_label='school', model='fundraising').get_all_objects_for_this_type().aggregate(
            Sum('earnings')
        ).get('earnings__sum'),
    }
    return render(request, f'{app}{sep}index.html', context)

@require_GET
def notice(request):
    return render(request, f'{app}{sep}messaging{sep}notice.html')

@require_GET
def message(request):
    return render(request, f'{app}{sep}messaging{sep}message.html')

@require_GET
def settings(request):
    return render(request, f'{app}{sep}settings{sep}main.html')

@require_GET
def allstudents(request):
    return render(request, f'{app}{sep}students{sep}all.html')

@require_GET
def allteachers(request):
    return render(request, f'{app}{sep}teachers{sep}all.html')

@require_GET
def allparents(request):
    return render(request, f'{app}{sep}parents{sep}all.html')

@require_GET
def allclassrooms(request):
    return render(request, f'{app}{sep}classrooms{sep}all.html')

@require_GET
def allattendances(request):
    context = {
        'month_days'  : [i for i in range(0, 31)],
        'month' : 'January',
        'year' : 2016,
        'class': ContentType.objects.get(app_label='classroom', model='classroom').get_object_for_this_type(pk=1),
    }
    return render(request, f'{app}{sep}classrooms{sep}attendence.html', context)

@require_GET
def allsubjects(request): # i.e admin//...//*.html
    return render(request, f'{app}{sep}classrooms{sep}subjects.html')

@require_GET
def allexams(request):
    return render(request, f'{app}{sep}exams{sep}all.html')

@require_GET
def allbooks(request):
    return render(request, f'{app}{sep}classrooms{sep}books.html')
@require_GET

def alltransport(request):
    return render(request, f'{app}{sep}transport{sep}all.html')

@require_GET
def allhostel(request):
    return render(request, f'{app}{sep}hostel{sep}all.html')

@require_GET
def allclasstimetable(request):
    return render(request, f'{app}{sep}classrooms{sep}timetable.html')

@require_GET
def allgrades(request):
    return render(request, f'{app}{sep}grading{sep}all.html')

