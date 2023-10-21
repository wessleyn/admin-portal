from django.db import models

class Department(models.Model):
    name = models.CharField( max_length=50)
    hod =  models.OneToOneField(
        'teacher.Teacher', 
        on_delete=models.SET_NULL,
        null=True,
        blank=True, 
        related_name='dep'
    )
   

    def has_Hod(self) -> bool:
        '''Does the departments have an hod?'''
        return True if self.hod is not None else False
    
    def number_of_members(self):
        '''
        Returns the number of teachers in a department
        '''
        return self.members.count()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'departments'