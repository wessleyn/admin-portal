from django.db import models
from apps.users.models import  CommonUser, StaffModel

 # TODO: add role or title assignment and reassignment to students

class Student(CommonUser):  
    academic_year = models.CharField(max_length=100, default='yyyy-yyyy')
    admission_date = models.DateField(auto_now_add=True)
    admission_id = models.CharField(max_length=50,  default='00000000')
    assignments = models.ManyToManyField('student.Assignment', blank=True)

    classroom = models.ForeignKey(
        'classroom.ClassRoom',
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='students'
    )

    parent = models.ForeignKey(
        'student.Parent', 
        related_name='children', 
        null=False, 
        blank=False,
        on_delete=models.CASCADE
    )

    combination = models.ForeignKey(
        'classroom.CombinationCategory',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        full_name = f'{self.last_name} {self.initial if self.initial else ""} {self.first_name}'
        return full_name
    
    def __repr__(self) -> str:
        return self.__str__()

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
        db_table = 'students'
        ordering = ['id']

class StudentAttendance(models.Model):
    data = models.BooleanField('Presence', default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendancies')

    def __str__(self) -> str:
        return f'Attendance for {str(self.student)}'

    class Meta:
        verbose_name = 'students_attendency'
        verbose_name_plural = 'students_attendencies'
        db_table = 'students_attendencies'


class Parent(StaffModel):
    d_o_b = None
    salary = None
    joining_date = None
    initial = None
    
    occupation = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'parent'
        verbose_name_plural = 'parents'
        db_table = 'parents'
    
class StudentReview(models.Model):
    # TOFIX: add weights for the student review choices
    choices = (
        ('0', 'Bad'),
        ('1', 'Average'),
        ('2', 'Good'),
        ('3', 'Best'),
    )

    choice = models.CharField(max_length=2, choices=choices)

    def get_review(self):
        '''
        Returns weight of the selected review
        '''
        if self.choice:
            for weight, choice in self.choices:
                if self.choice.lower() == choice.lower():
                    return int(weight)
        else:
            return 0

    class Meta:
        verbose_name = 'student_review'
        verbose_name_plural = 'student_reviews'
        db_table = 'students_reviews'

class Assignment(models.Model):
    subject = models.OneToOneField(
        'classroom.Subject', 
        related_name='assignments', 
        on_delete=models.CASCADE
    )
    due = models.DateTimeField(auto_now_add=False, auto_created=False, auto_now=False)

    class Meta:
        db_table = 'assignments'
        
class Session(models.Model):
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return "From " + str(self.start) + " to " + str(self.end)

class LeaveReportStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.CharField(max_length=60)
    message = models.TextField()
    status = models.SmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeedbackStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class NotificationStudent(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StudentResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey('classroom.Subject', on_delete=models.CASCADE)
    test = models.FloatField(default=0)
    exam = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
