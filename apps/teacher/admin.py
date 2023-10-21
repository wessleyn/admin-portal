from django.contrib import admin
from apps.hod.models import *
from apps.teacher.models import Teacher

# Styling for Department Model
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'number_of_members',
        'has_Hod'

    ]
    exclude = [
        'supervisor'
    ]

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    ...