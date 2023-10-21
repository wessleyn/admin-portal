from django.db import models
from apps.users.models import  StaffModel

class Deputy(StaffModel):
    optional_job = models.OneToOneField(
        'teacher.Teacher', 
        verbose_name="Optional_Job",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def number_of_departments(self):
        return self.departments.count()
    
    # def __init__(self, *args, **kwargs) -> None:
    #     super().__init__(*args, **kwargs)

    class Meta:
        verbose_name = 'deputy'
        verbose_name_plural =  'deputies'
        db_table = 'deputy'

class Dean(StaffModel):
    class Meta:
        verbose_name = 'dean'
        verbose_name_plural =  'dean'
        db_table = 'dean'
