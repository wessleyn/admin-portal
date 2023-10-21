from rest_framework.serializers import ModelSerializer, ImageField, SerializerMethodField
from django.contrib.contenttypes.models import ContentType
from api.serializers.common import PhoneNumberSerializer

Vehicle = ContentType.objects.get(app_label='school', model='vehicle').model_class()
Hostel = ContentType.objects.get(app_label='school', model='hostel').model_class()

class VehicleSerializer(ModelSerializer): 
    driver = SerializerMethodField()
    contact = SerializerMethodField()
    driver_license = SerializerMethodField()
    

    class Meta:
        model = Vehicle
        fields = [
            'route',
            'no',
            'driver',
            'driver_license',
            'contact',
        ]
    
    def get_driver(self, obj):
        return obj.driver.full_name
    
    def get_driver_license(self, obj):
        return obj.driver.driver_license
    
    def get_contact(self, obj):
        # data = PhoneNumberSerializer(data={"number": obj.driver.contact})
        # data = data.get_value()
        # print(data)
        return str(obj.driver.contact.raw_input)
    
class HostelSerializer(ModelSerializer): 
    student = SerializerMethodField()
    
    class Meta:
        model = Hostel
        fields = [
            'name',
            'no',
            'ty',
            'n_bed',
            'number_of_students',
        ]

    