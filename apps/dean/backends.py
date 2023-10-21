from django.contrib.auth.backends import BaseBackend
from apps.dean.models import Dean, Deputy

class DeanLoginBackend(BaseBackend):
    def get_user(self, user_id):
        try:
            return Dean.objects.get(pk=user_id)
        except Dean.DoesNotExist:
            try:
                return Deputy.objects.get(pk=user_id)
            except Deputy.DoesNotExist:
                return None
        
    def authenticate(self, request, username=None, password=None):
        '''
        Checks the credentials against the database
        '''
        try:
            user =  Dean.objects.get(email=username)
            return user if password == user.password else None
        except Dean.DoesNotExist:
            try:
                user = Deputy.objects.get(email=username)
                return user if password == user.password else None
            except Deputy.DoesNotExist:
                return None