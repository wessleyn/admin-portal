from django.shortcuts import render, get_object_or_404, redirect
from teacher.models import Teacher
from teacher.forms import CreateTeacher
from django.contrib import messages
from apps.users.models import  CommonUser

id = CommonUser.get_identity

parent = 'dean/teachers/'


def single_teacher(request, teacher_id):
    caller = id(request.user.identity) + '/index.html'
    single_teacher = get_object_or_404(Teacher, pk=teacher_id)
    context = {
        'caller': caller,
        "single_teacher": single_teacher
    }
    return render(request, parent + "single_teacher.html", context)


def create_teacher(request):
    caller = id(request.user.identity) + '/index.html'
    if request.method == "POST":
        forms = CreateTeacher(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "Teacher Registration Successfully!")
        return redirect("teacher_list")
    else:
        forms = CreateTeacher()

    context = {
        'caller': caller,
        "forms": forms
    }
    return render(request, parent + "create_teacher.html", context)


def edit_teacher(request, pk):
    caller = id(request.user.identity) + '/index.html'
    teacher_edit = Teacher.objects.get(id=pk)
    edit_teacher_forms = CreateTeacher(instance=teacher_edit)

    if request.method == "POST":
        edit_teacher_forms = CreateTeacher(
            request.POST, request.FILES or None, instance=teacher_edit)

        if edit_teacher_forms.is_valid():
            edit_teacher_forms.save()
            messages.success(request, "Edit Teacher Info Successfully!")
            return redirect("teacher_list")

    context = {
        'caller': caller,
        "edit_teacher_forms": edit_teacher_forms
    }
    return render(request, parent + "edit_teacher.html", context)


def delete_teacher(request, teacher_id):
    teacher_delete = Teacher.objects.get(id=teacher_id)
    teacher_delete.delete()
    messages.success(request, "Delete Teacher Info Successfully")
    return redirect("teacher_list")
