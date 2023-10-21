from django.contrib import admin
from apps.classroom.models import *

@admin.register(CombinationCategory)
class CombinationAdmin(admin.ModelAdmin):
    extra = 3
    list_display = [
        'name',
        'number_of_subjects',
        # 'subjects' Display a list of subjects per category 
    ]
    
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'syllabus_code',
        'combination_category',
        'number_of_teachers',
        'number_of_sub_teachers'
    ]

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = [
        '__str__',
        'combination',
        'number_of_students',
        'number_of_subjects'
    ]


