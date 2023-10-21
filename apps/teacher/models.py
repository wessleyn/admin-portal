from django.db import models
from apps.users.models import   StaffModel

class Teacher(StaffModel):

    department = models.ForeignKey(
        "hod.Department", 
        on_delete=models.CASCADE, 
        related_name='members', 
        null=True, 
        blank=True
    ) 

    subject = models.ForeignKey(
        'classroom.Subject', 
        on_delete=models.CASCADE, 
        related_name='teachers'
    ) 
    
    # An emergency / part-time subject
    optional_subject = models.ForeignKey(
        'classroom.Subject', 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        related_name='sub_teachers'
    ) 
  
    # The classroom where the subject is taught
    teaching_classrooms = models.ManyToManyField(
        'classroom.Classroom', 
        related_name='subject_teachers'
    )
    
    assessments = models.ManyToManyField('teacher.Assessment', related_name='teachers')
    student_review = models.ManyToManyField('student.StudentReview', related_name='teachers_reviews')

    def last_assessment(self):
        return self.assessments.last()

    def due_assessment(self):
        return self.assessments.filter(due=True).last()

    def number_of_classrooms(self) -> int:
        return self.teaching_classrooms.count()

    def classroom_names(self) -> list[str]:
        names = [str(i) for i in self.teach_class.all()]
        return names

    # TODO: implement this method
    def reviews(self):
        '''
        Calculates the students reviews using an algorithm 
        where the bad student decreases the review and good 
        increases. However the weight of the decrease or 
        increase is based on the quality of review
        i.e best might be +4 and good will be +2
        '''
        from random import randint
        return randint(0, 100)

    class Meta:
        db_table = 'teachers'

class Assessment(models.Model):

    name = models.CharField(max_length=15)

    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)

    due = models.BooleanField(default=False)

    # TODO: Rethink this field location, should it be in Teacher or Student and what API should be exposed? And How?
    result = models.PositiveSmallIntegerField(blank=True, default=0)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'assessment'
        verbose_name_plural = 'assessments'
        db_table = 'assessments'
