from rest_framework.serializers import ModelSerializer, ImageField, SerializerMethodField
from django.contrib.contenttypes.models import ContentType

Teacher = ContentType.objects.get(app_label='teacher', model='teacher').model_class()

class TeacherSerializer(ModelSerializer): 
    first_name = SerializerMethodField()
    subject = SerializerMethodField()
    
    profile_pic = ImageField(
        read_only=True,
    )
    
    class Meta:
        model = Teacher
        fields = [
            'id',
            'profile_pic',
            'first_name',
            'gender',
            'subject',
            'address',
            'email',
            
        ]
    
    def get_first_name(self, obj):
        return str(obj)
    
    def get_subject(self, obj):
        return str(obj.subject)
    

