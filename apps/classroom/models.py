from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=20)
    threshold = models.CharField(max_length=6)
    fro = models.CharField('From', max_length=6)
    to = models.CharField('To', max_length=6)
    comment = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'grade'
        verbose_name_plural = 'grades'
        db_table = 'grade_book'

class CombinationCategory(models.Model):
    name = models.CharField(max_length=20)
    
    def subjects(self):
        return self.subjects.all()

    def number_of_subjects(self):
        return self.subjects.count()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'combination_category'
        verbose_name_plural = 'combination_categories'
        db_table = 'combination_categories'

class Subject(models.Model):
    name = models.CharField(max_length=20)
    syllabus_code = models.CharField(max_length=5, unique=True)
    syllabus_link = models.URLField(blank=True)
    combination_category = models.ForeignKey(
        'CombinationCategory',
        on_delete=models.CASCADE,
        related_name='subjects',
        default=1 # Default one will be required in setup
    )

    def number_of_teachers(self):
        return self.teachers.count()

    def number_of_sub_teachers(self):
        return self.sub_teachers.count()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'subject'
        db_table = 'subjects'

class Exam(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    time = models.CharField(max_length=140)
    subject = models.ForeignKey(
        Subject,
        related_name='exams', 
        null=False, 
        blank=False,
        on_delete=models.CASCADE
    )
    date = models.DateField(null=False, blank=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'exam'
        verbose_name_plural = 'exams'
        db_table = 'exams'

class Book(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    author = models.CharField(max_length=140)
    subject = models.ForeignKey(
        Subject,
        related_name='books', 
        null=False, 
        blank=False,
        on_delete=models.CASCADE
    )

    edition = models.CharField(max_length=3)
    isbn = models.CharField(max_length=255)
    quantity = models.SmallIntegerField(null=True, blank=True, default=1)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        db_table = 'books'

class ClassRoom(models.Model):
    name = models.CharField(max_length=10)
    grade = models.PositiveSmallIntegerField()
    subjects = models.ManyToManyField('Subject', through='ClassInformation')
    combination = models.ForeignKey(
        CombinationCategory, 
        on_delete=models.CASCADE
    )
    class_teacher = models.OneToOneField(
        'teacher.Teacher', on_delete=models.SET_NULL, blank=False, null=True)

    def class_teacher_name(self) -> str:
        return str(self.class_teacher)

    def subjects_list(self):
        self.classroom.populate_subjects()  # get subject from combination category
        return list(self.classroom.subjects.all())

    # Figures

    def number_of_students(self) -> int:
        num = self.classroom.students.count()
        return num

    def number_of_subjects(self) -> int:
        self.classroom.populate_subjects()
        return self.classroom.subjects.count()

    def number_of_students(self):
        return self.students.count()
    
    def number_of_subjects(self):
        return self.subjects.count()

    # Internal
    def populate_subjects(self):
        ''' Assigns a  classroom  subjects from its combination category'''
        self.subjects.set(
            Subject.objects.filter(combination_category=self.combination.pk)
        )
    

    def __str__(self) -> str:
        return f'{self.grade} {self.name}'
   
    def __repr__(self) -> str:
        return f'{self.grade} {self.name}'

    class Meta:
        verbose_name = 'classroom'
        db_table = 'classes'

class ClassAttendance(models.Model):
    classroom = models.ForeignKey(ClassRoom, related_name='attendance_records', on_delete=models.CASCADE)
    month = models.CharField(max_length=50)
    year = models.CharField(max_length=5)
    students = models.ManyToManyField('student.StudentAttendance', blank=True, related_name='class_attendance_records')

    def __str__(self) -> str:
        return f'Attendance Record for {str(self.classroom)} : {self.month}, {self.year}'

    class Meta:
        verbose_name = 'class_attendance'
        db_table = 'class_attendancies'

class ClassTimetable(models.Model):
    month = models.CharField(max_length=20)
    year = models.CharField(max_length=5)
    classroom = models.ForeignKey(ClassRoom, related_name='timetable', on_delete=models.CASCADE)
    day = models.CharField(max_length=20)
    subject = models.OneToOneField(Subject, related_name='timetables', on_delete=models.CASCADE)
    period  = models.CharField(max_length=20)
    teacher = models.ForeignKey('teacher.Teacher', related_name='timetables', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Timetable for {str(self.classroom)} : {self.month}, {self.year}'

    class Meta:
        verbose_name = 'class_timetable'
        db_table = 'class_timetables'

# Consider putting a isSpecial methodfor special classes
class ClassInformation(models.Model):
    '''
    A read only model for accessing a class_room level information
    '''
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    subjects = models.ForeignKey(
        Subject, on_delete=models.CASCADE, blank=True, null=True)  # aesthetics
    class_teacher = models.OneToOneField(
        'teacher.Teacher', on_delete=models.SET_NULL, blank=False, null=True)

    def class_teacher_name(self) -> str:
        return str(self.class_teacher)

    def subjects_list(self):
        self.classroom.populate_subjects()  # get subject from combination category
        return list(self.classroom.subjects.all())

    # Figures

    def number_of_students(self) -> int:
        num = self.classroom.students.count()
        return num

    def number_of_subjects(self) -> int:
        self.classroom.populate_subjects()
        return self.classroom.subjects.count()

    def __str__(self) -> str:
        return f'{self.classroom} - {self.subject}'

    class Meta:
        verbose_name = 'class_information'
        verbose_name_plural =  'class_information'
        db_table = 'class_information'
