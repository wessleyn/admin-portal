from django.test import TestCase
from apps.dean.models import Deputy
from apps.hod.models import Department
from apps.teacher.models import Teacher
from apps.classroom.models import Subject, CombinationCategory

class TestDep(TestCase):
    def setUp(self) -> None:
        self.all = CombinationCategory.objects.create(name='__all__')
        self.lit = Subject.objects.create(name='English Literature', syllabus_code='0580',combination_category=self.all)
        self.en = Subject.objects.create(name='English First Language', syllabus_code='0588',combination_category=self.all)
        self.fre = Subject.objects.create(name='French', syllabus_code='0900',combination_category=self.all)

        Deputy.objects.create(
            email='dean@c.com',

            d_o_b='1999-1-2',
            first_name='John',
            last_name='Smith',
            gender='Male',
        )

        # Departement
        self.dp = Department.objects.create(
            name = 'Literature',
        )

        # Teachers
        self.t1 = Teacher.objects.create(
            first_name='mmm',
            last_name='Smith',
            d_o_b='1999-1-2',
            email='test@c.com',
            gender='Male',
            department = self.dp,
            subject=self.fre,
            optional_subject=self.en
        )
    
    def test_has_hod(self): 
        self.assertFalse(self.dp.has_Hod())
    
    # bad idea assignning an hod like this: revisit later
    def test_number_of_members(self):
        '''Test that the hod is not counted twice'''
        self.assertEqual(self.dp.number_of_members(), 1)
        self.dp.hod = self.t1
        self.dp.hod.save()
        self.assertTrue(self.dp.has_Hod())
        self.assertEqual(self.dp.number_of_members(), 1) # 2 then a bug

   