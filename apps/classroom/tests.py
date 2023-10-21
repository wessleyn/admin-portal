from django.test import TestCase
from apps.dean.models import Deputy
from apps.classroom.models import *
from apps.student.models import Student, Parent
from apps.hod.models import Department
from apps.teacher.models import Teacher


class TestClassroom(TestCase):
    def setUp(self) -> None:
        Deputy.objects.create(
            email='dean@c.com',
            first_name='John',
            last_name='Smith',
            gender='Male',
            d_o_b='1968-02-09',
        )
        d = Department.objects.create(
            name='xXx',
        )
        # Categories
        self.scFi = CombinationCategory.objects.create(name='Sciences')
        self.arts = CombinationCategory.objects.create(name='Arts')
        self.comm = CombinationCategory.objects.create(name='Commercials')
        self.all = CombinationCategory.objects.create(name='all')

        # Subjects
        self.math = Subject.objects.create( name='Maths', syllabus_code='0580', combination_category=self.all)
        self.phys = Subject.objects.create(name='Physics', syllabus_code='0900', combination_category=self.scFi)
        self.chem = Subject.objects.create(name='Chemistry', syllabus_code='0930', combination_category=self.scFi)
        self.hist = Subject.objects.create(name='History', syllabus_code='0221', combination_category=self.arts)

        # Teachers
        self.t1 = Teacher.objects.create(
            first_name='John',
            last_name='Smith',
            d_o_b='1898-12-12',
            email='test1@c.com',
            gender='Male',
            department=d,
            subject=self.math
        )
        self.t2 = Teacher.objects.create(
            first_name='Rue ',
            last_name='Mayball',
            email='test2@c.com',
            gender='Female',
            department=d,
            subject=self.phys,
            optional_subject = self.chem,
            d_o_b='1898-12-12'
        )
        self.t3 = Teacher.objects.create(
            first_name='Rose',
            last_name=' Smith',
            d_o_b='1898-1-2',
            email='test3@c.com',
            gender='Female',
            department=d,
            subject=self.hist
        )

        # class
        f4 = ClassRoom.objects.create(
            name='Fountain',
            grade=4,
            combination=self.scFi
        )
        # Assignment
        f4.subjects.add(self.math)
        f4.save()

        # ClassRooms
        self.clas1 = ClassInformation.objects.create(
            classroom=f4,
            class_teacher=self.t2
        )
        self.clas2 = ClassInformation.objects.create(
            classroom=ClassRoom.objects.create(
                name='Oasis',
                grade=4,
                combination=self.arts,
            ),
            class_teacher=self.t1,
        )

    def test_name(self):
        self.assertEqual(str(self.scFi), 'Sciences')
        self.assertEqual(str(self.clas1.classroom.name), 'Fountain')
        self.assertEqual(self.clas1.class_teacher_name(), str(self.t2))

    def test_number_of_sub_teachers(self):
        self.assertEqual(self.math.number_of_sub_teachers(), 0)  
        self.assertEqual(self.phys.number_of_sub_teachers(), 0)  
        self.assertEqual(self.chem.number_of_sub_teachers(), 1)  

    def test_number_of_teachers(self):
        Teacher.objects.create(
            first_name='xxx',

            d_o_b='1898-1-2',
            last_name='Smith',
            email='tesst@c.com',
            gender='Male',
            department=Department.objects.create(
                name='xXx',
            ),
            subject=self.math
        )
        self.assertEqual(self.math.number_of_teachers(), 2)

    def test_num_students(self):
        '''
        Students with an implicit relationship to a cassroom are accessible to the coresponding information class (backward relationship)
        '''
        self.assertEqual(self.clas1.number_of_students(), 0)
        Student.objects.create(  
            email = 'test@test.com',
            last_name='Wessley',
            d_o_b='2000-1-2',
            initial='J',
            first_name='John',
            parent=Parent.objects.create(email='teast@c.com',last_name='Non', first_name='John'),
            classroom=self.clas1.classroom,
        )
        self.assertEqual(self.clas1.number_of_students(), 1)


    def test_num_subjects(self):
        self.assertEqual(
            self.clas1.number_of_subjects(),
            2
        )

    def test_subjects_list(self):
        self.assertListEqual(
            self.clas1.subjects_list(),
            [self.phys, self.chem]
        )

        self.assertEqual(
            self.scFi.number_of_subjects(),
            2
        )

    def teacher_number_of_classrooms(self):
        self.assertEqual(
            self.t1.teach_class.all(),
            0
        )
        self.t1.teach_class.add(self.clas1)
        self.t1.save()
        self.assertEqual(
            self.t1.teach_class.all(),
            2
        )