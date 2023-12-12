from django.shortcuts import get_object_or_404
import json

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics

from api.serializers.students import StudentSerializer, Student
from api.serializers.teachers import TeacherSerializer, Teacher
from api.serializers.parents import ParentSerializer, Parent
from api.serializers.classroom import ClassRoomSerializer, ClassRoom, SubjectSerializer, Subject
from api.serializers.classroom import BookSerializer, Book, ClassAttendance, Exam, ExamSerializer
from api.serializers.classroom import ClassTimeTableSerializer, ClassTimeTable, GradeSerializer
from api.serializers.classroom import Grade
from api.serializers.school import Vehicle, VehicleSerializer, Hostel, HostelSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'all-students': reverse('all-students-list', request=request, format=format),
        'all-teachers': reverse('all-teachers-list', request=request, format=format),
        'all-parents': reverse('all-parents-list', request=request, format=format),
        'all-classrooms': reverse('all-classrooms-list', request=request, format=format),
        'all-subjects': reverse('all-subjects-list', request=request, format=format),
        'all-books': reverse('all-books-list', request=request, format=format),
        'all-exams': reverse('all-exams-list', request=request, format=format),
        'all-grades': reverse('all-grades-list', request=request, format=format),
        'all-vehicles': reverse('all-vehicles-list', request=request, format=format),
        'all-hostels': reverse('all-hostels-list', request=request, format=format),
        'all-attendencies': reverse('all-attendencies-list', request=request, format=format),
    })


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class HostelList(generics.ListCreateAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ParentList(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ClassRoomList(generics.ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ExamList(generics.ListCreateAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class GradeList(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    
class ClassTimeTableList(generics.ListCreateAPIView):
    queryset = ClassTimeTable.objects.all()
    serializer_class = ClassTimeTableSerializer

class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class AttendencyDetail(APIView):

    def serialize(self, month=None, year=None):
        students = [
            {
                "name": str(student),
                # TODO: Filter the attendencies by year and month
                "record": [int(attandance.data) for attandance in student.attendancies.all()]
            }
            for student in self.classroom.students.all()
        ]

        # Serialize the data to JSON
        return json.loads(json.dumps(students))


    def get(self, request, pk, format=None):
        self.classroom = ClassRoom.objects.get(pk=1)
        return Response(self.serialize())