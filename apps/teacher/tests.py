from django.test import TestCase
from classroom. models import *
from hod.models import Deputy
from hod.models import Department
from teacher.models import Teacher

# Object Test

class TestTeacher(TestCase):
    def setUp(self):
        self.category = CombinationCategory.objects.create(name='__all__')
        self.subject = Subject.objects.create(
            name='English',
            syllabus_code='0589',
            combination_category=self.category
        )

        Deputy.objects.create(
            email='dean@c.com',
            first_name='John',
            last_name='Smith',
            gender='Male',
        )

        d = Department.objects.create(
            name='xXx',
        )
        
        self.t1 = Teacher.objects.create(
            first_name='John',
            last_name='Smith',
            email='test@c.com',
            gender='Male',
            department=d,
            subject=self.subject
        )

    def test_name(self):
        self.assertEqual(str(self.t1), 'Sir Smith')

    def test_subject(self):
        self.assertEqual(self.t1.subject.name, 'English')

    def test_gender(self):
        self.assertEqual(self.t1.gender, 'Male')

    def test_number_of_classrooms(self):
        self.assertFalse(self.t1.number_of_classrooms())
    
# User Test : pending