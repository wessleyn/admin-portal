from rest_framework.serializers import ModelSerializer, ImageField, SerializerMethodField
from random import randint, choice
from django.contrib.contenttypes.models import ContentType

Student = ContentType.objects.get(app_label='student', model='student').model_class()



class StudentSerializer(ModelSerializer): 
    parent = SerializerMethodField()
    classroom = SerializerMethodField()
    fees = SerializerMethodField()
    status = SerializerMethodField()
    
    profile_pic = ImageField(
        read_only=True,
        # source=Student.profile_pic
        # use_url=False
    )
    
    class Meta:
        model = Student
        fields = [
            'id',
            'profile_pic',
            '__str__',
            'gender',
            'classroom',
            'parent',
            'address',
            'd_o_b',
            'fees',
            'status',
            'email',
        ]
    

    def get_fees(self, obj):
        # Generate 10 random numbers between 0 and 700
        fees = [randint(0, 700) for _ in range(10)]
        fees.append(0)  # Add a 0 to the list of fees
        self.fees = choice(fees)
        return self.fees # Return a random fee from the list
    
    def get_status(self, obj):
        return 'Paid' if self.fees == 0 else  'Unpaid'

    def get_parent(self, obj):
        return str(obj.parent)

    def get_classroom(self, obj):
        return str(obj.classroom)
    

