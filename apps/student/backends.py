from django.contrib.auth.backends import BaseBackend
from apps.student.models import Student

class StudentLoginBackend(BaseBackend):
    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
        
    def authenticate(self, request, username=None, password=None):
        '''
        Checks the credentials against the database
        '''
        try:
            user =  Student.objects.get(email=username)
            return user if password == user.password else None
        except Student.DoesNotExist:
            return None