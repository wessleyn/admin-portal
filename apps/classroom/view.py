from django.shortcuts import render, get_object_or_404, redirect
from classroom.models import ClassRoom 
from classroom.forms import CreateClassroom
from django.contrib import messages
from django.core.paginator import Paginator
from apps.users.models import  CommonUser

id = CommonUser.get_identity

parent = 'classroom/'

def class_list(request):
    caller = id(request.user.identity) + '/index.html'
    classrooms = ClassRoom.objects.all()

    paginator = Paginator(classrooms, ClassRoom.objects.count())
    page = request.GET.get('page')
    paged_classrooms = paginator.get_page(page)
    context = {
        'caller': caller,
        "classrooms": paged_classrooms
    }
    return render(request, parent + "class_list.html", context)

def single_class(request, class_id):
    caller = id(request.user.identity) + '/index.html'
    single_classroom = get_object_or_404(ClassRoom, pk=class_id)
    context = {
        'caller': caller,
        "single_class": single_classroom
    }
    return render(request, parent + "single_class.html", context)


def create_class(request):
    caller = id(request.user.identity) + '/index.html'
    if request.method == "POST":
        forms = CreateClassroom(request.POST, request.FILES or None)

        if forms.is_valid():
            forms.save()
        messages.success(request, "classroom Registration Successfully!")
        return redirect("classroom_list")
    else:
        forms = CreateClassroom()

    context = {
        'caller': caller,
        "forms": forms
    }
    return render(request, parent + "create_class.html", context)


def edit_class(request, pk):
    caller = id(request.user.identity) + '/index.html'
    classroom_edit = ClassRoom.objects.get(id=pk)
    edit_classroom_forms = CreateClassroom(instance=classroom_edit)

    if request.method == "POST":
        edit_classroom_forms = CreateClassroom(
            request.POST, request.FILES or None, instance=classroom_edit)

        if edit_classroom_forms.is_valid():
            edit_classroom_forms.save()
            messages.success(request, "Edit classroom Info Successfully!")
            return redirect("classroom_list")

    context = {
        'caller': caller,
        "edit_class_forms": edit_classroom_forms
    }
    return render(request, parent + "edit_class.html", context)


def delete_class(request, classroom_id):
    classroom_delete = ClassRoom.objects.get(id=classroom_id)
    classroom_delete.delete()
    messages.success(request, "Delete classroom Info Successfully")
    return redirect("classroom_list")
