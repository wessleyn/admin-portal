from django.test import TestCase
from apps.student.models import Student
from apps.classroom.models import ClassRoom, CombinationCategory, Subject, ClassInformation
from .models import Student, Parent, StudentReview, Assignment, Session, LeaveReportStudent, FeedbackStudent, NotificationStudent, StudentResult
from apps.teacher.models import Teacher
from apps.hod.models import Department
from apps.dean.models import Deputy


class TestStudentAppModels(TestCase):
    '''
    Test the Student Business Logic At a Database level
    '''

    def setUp(self) -> None:
        #  Departments to avoid unique contraint
       
        Deputy.objects.create(
            email='dean@c.com',
            first_name='John',
            last_name='Smith',
            gender='Male',
            d_o_b =  '1930-1-1'
        )

        d = Department.objects.create(name='xXx',)

        self.cat1 = CombinationCategory.objects.create(name='Sciences')
        self.cat2 = CombinationCategory.objects.create(name='Arts')
        self.cat3 = CombinationCategory.objects.create(name='__all__')
        
        self.sub1 = Subject.objects.create(
            name='English',
            syllabus_code='0599',
            combination_category=self.cat3,
        )
        
        self.sub2 = Subject.objects.create(
            name='Maths',
            syllabus_code='0590',
            combination_category=self.cat3
        )
        
        self.sub3 = Subject.objects.create(
            name='History',
            syllabus_code='0200',
            combination_category=self.cat2
        )

        self.cls1 = ClassRoom.objects.create(
            name='Fountain',
            grade=4,
            # subjects = (self.sub1, self.sub2),
            combination=self.cat1
        )
        self.cls2 = ClassRoom.objects.create(
            name='Oasis',
            grade=4,
            # subjects = (self.sub1, self.sub2, self.sub3),
            combination=self.cat2
        )

        self.normal_parent = Parent.objects.create(
            email='teast@c.com',
            last_name='Non',
            first_name='John',
        )
        self.normal_student = Student.objects.create(  
            email = 'test@c.com',
            last_name='Wessley',
            initial='J',
            first_name='John',
            classroom=self.cls1,
            d_o_b='2000-9-4',
            parent=self.normal_parent
        )
        
        self.flexy_parent = Parent.objects.create(  
            email = 'goaku@test.com',
            last_name='Chriasastian',
            first_name='Joasashn',
        )

        self.flexy_ = Student.objects.create(  
            email = 'goku@test.com',
            last_name='Christian',
            first_name='John',
            classroom=self.cls2,
            combination=self.cat2,
            d_o_b='2001-9-4',
            parent = self.flexy_parent
        )
        self.t1 = Teacher.objects.create(
            email='mark@c.com',
            last_name='John',
            first_name='Smith',
            gender='Male',
            department=d,
            subject=self.sub1,
            d_o_b='2010-9-4'
        )
        _ = ClassInformation.objects.create(
            classroom=self.cls1,
            class_teacher=self.t1
        )
        _.classroom.subjects.set([self.sub1, self.sub2])
        _.save()

    def test_str_return(self):
        self.assertEqual(str(self.cat1), 'Sciences')
        self.assertEqual(str(self.cat2), 'Arts')
        self.assertEqual(str(self.cat3), '__all__')
        self.assertEqual(str(self.sub1), 'English')
        self.assertEqual(str(self.sub2), 'Maths')
        self.assertEqual(str(self.sub3), 'History')
        self.assertEqual(str(self.cls1), '4 Fountain')
        self.assertEqual(str(self.cls2), '4 Oasis')
        self.assertEqual(str(self.normal_student), 'Wessley J John')
        self.assertEqual(str(self.flexy_), 'Christian  John')

    def test_combination_category(self):
        self.assertEqual(self.cat1.number_of_subjects(), 0)
        self.assertEqual(self.cat2.number_of_subjects(), 1)
        self.assertEqual(self.cat3.number_of_subjects(), 2)

    def test_student_classroom_name(self):
        self.assertEqual(self.normal_student.classroom.name, 'Fountain')
        self.assertEqual(self.flexy_.classroom.name, 'Oasis')

    def test_student_classroom_combination(self):
        self.assertEqual(self.flexy_.classroom.combination.name, 'Arts')
        self.assertEqual(
            self.normal_student.classroom.combination.name, 'Sciences')

    def test_student_classroom_subjects(self):
        self.assertEqual(tuple(self.normal_student.classroom.subjects.all()), (self.sub1, self.sub2))
        self.assertFalse(bool(self.flexy_.classroom.subjects.all()))  # Empty

    def test_student_re_asssignment_classroom(self):
        self.assertEqual(Student.objects.filter(classroom=self.cls1).count(), 1)
        self.flexy_.classroom = self.cls1
        self.flexy_.save()
        self.assertEqual(self.flexy_.classroom.name, 'Fountain')
        self.assertEqual(Student.objects.filter(
            classroom=self.cls1).count(), 2)

    def test_student_auto_subjects_by_combination(self):
        self.normal_student.classroom = None
        self.normal_student.save()
        self.assertIsNone(self.normal_student.classroom)
        # self.assertEqual(self.normal_student.combination.subjects.count(), 1)
        # self.assertEqual(self.flexy_.combination.subjects.count(), 1)
