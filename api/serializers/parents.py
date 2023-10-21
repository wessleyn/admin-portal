from rest_framework.serializers import ModelSerializer, ImageField, SerializerMethodField
from django.contrib.contenttypes.models import ContentType

Parent = ContentType.objects.get(app_label='student', model='parent').model_class()

class ParentSerializer(ModelSerializer): 
    first_name = SerializerMethodField()
    
    profile_pic = ImageField(
        read_only=True,
    )
    
    class Meta:
        model = Parent
        fields = [
            'id',
            'profile_pic',
            'first_name',
            'gender',
            'occupation',
            'address',
            'email',
            
        ]
    
    def get_first_name(self, obj):
        return str(obj)
