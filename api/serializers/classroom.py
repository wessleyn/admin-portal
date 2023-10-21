from rest_framework.serializers import ModelSerializer, URLField, SerializerMethodField
from django.contrib.contenttypes.models import ContentType
from os import system as sys
cls = lambda: sys('cls')

ClassRoom = ContentType.objects.get(app_label='classroom', model='classroom').model_class()
ClassAttendance = ContentType.objects.get(app_label='classroom', model='classattendance').model_class()

Subject = ContentType.objects.get(app_label='classroom', model='subject').model_class()
Book = ContentType.objects.get(app_label='classroom', model='book').model_class()
Exam = ContentType.objects.get(app_label='classroom', model='exam').model_class()
Grade = ContentType.objects.get(app_label='classroom', model='grade').model_class()
ClassTimeTable = ContentType.objects.get(app_label='classroom', model='classtimetable').model_class()

class ClassRoomSerializer(ModelSerializer):
    combination = SerializerMethodField()
    class_teacher = SerializerMethodField()
    
    class Meta:
        model = ClassRoom
        fields = [
            'id',
            '__str__',
            'combination',
            'class_teacher',
            'number_of_students',
            
        ]
    
    def get_combination(self, obj):
        return str(obj.combination)

    def get_class_teacher(self, obj):
        return str(obj.class_teacher)

class ClassTimeTableSerializer(ModelSerializer):
    subject = SerializerMethodField()
    teacher = SerializerMethodField()

    class Meta:
        model = ClassTimeTable
        fields = [
            'day', 
            'subject', 
            'teacher', 
            'period'
        ]
    
    def get_subject(self, obj):
        return str(obj.subject)

    def get_teacher(self, obj):
        return str(obj.teacher)

class SubjectSerializer(ModelSerializer):
    combination_category = SerializerMethodField()
    syllabus_link = URLField()
    
    class Meta:
        model = Subject
        fields = [
            'id',
            '__str__',
            'combination_category',
            'syllabus_code',
            'syllabus_link',
            'number_of_teachers'
        ]
    
    def get_combination_category(self, obj):
        return str(obj.combination_category)

class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grade
        fields = [
            'name',
            'threshold',
            'fro',
            'to',
            'comment',
        ]

class ExamSerializer(ModelSerializer):
    subject = SerializerMethodField()
    
    class Meta:
        model = Exam
        fields = [
            'id',
            '__str__',
            'subject',
            'time',
            'date',
        ]
    
    def get_subject(self, obj):
        return str(obj.subject)

class BookSerializer(ModelSerializer):
    subject = SerializerMethodField()
    
    class Meta:
        model = Book
        fields = [
            'id',
            '__str__',
            'subject',
            'author',
            'edition',
            'isbn',
            'quantity'
        ]
    
    def get_subject(self, obj):
        return str(obj.subject)
