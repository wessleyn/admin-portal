from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group, Permission
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.admin import ModelAdmin
from django.utils import timezone
from django.db import models
     
class CommonManager(BaseUserManager):
    def create_user(self, email, password=None, *args, **kwargs):
        """
        Creates and saves a User with the given email password.
        """
        if not email:
            raise ValueError("Users must have an email address")
            
        user = self.model(
            email=self.normalize_email(email),
        )
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password=None, *args, **kwargs):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
       
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class CommonUser(AbstractBaseUser):
    '''
    Defines common fields for users of the platform
    '''
    GENDER = [('M', 'Male'), ('F', 'Female')]
    USER_TYPES = [
        ('1', 'Dean'),
        ('2', 'Deputy'),
        ('3', 'Hod'),
        ('4', 'Teacher'),
        ('5', 'Student'),
        ('6', 'Admin'),
        ('7', 'Parent'),
        ('8', 'Driver'),

    ]

    last_name = models.CharField(
        max_length=40,
        db_index=True
    )
    initial = models.CharField(
        max_length=3,
        blank=True,
    )
    first_name = models.CharField(
        max_length=80
    )

    religion = models.CharField(max_length=90)
    d_o_b = models.DateField('Date of Birth', blank=False, null=False)
    address = models.TextField('Address', blank=False, null=False)
    id_no = models.CharField('Identification Number', max_length=25)
    profile_pic = models.ImageField(upload_to='images/avatar/profile', null=True)
    gender = models.CharField(max_length=8, choices=GENDER)

    # Permissions
    user_permissions = models.ManyToManyField(Permission)

    # Grouping
    groups = models.ManyToManyField(Group)

    # required attr
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) # access to the admin page
    is_superuser = models.BooleanField(default=False)

    # Authorization
    email = models.EmailField(verbose_name='Email address', unique=True)
    identity = models.CharField(max_length=2, choices=USER_TYPES)

    # Manager
    objects = CommonManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @staticmethod
    def get_identity(identity):
        for x, y in CommonUser.USER_TYPES:
            if x == str(identity):
                return y

    def has_module_perms(self, *args, **kwargs):
        return True
   
    def has_perm(self, *args, **kwargs):
        return True
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.initial} {self.last_name}'
    
    class Meta:
        ordering = ['id_no']
        abstract = True

class CommonAdmin(ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ['last_name', 'first_name', 'gender'],
        }),
    )

class StaffModel(CommonUser):
    salary = models.PositiveSmallIntegerField(default=0)
    contact = PhoneNumberField('+263', blank=True, null=True)
    joining_date = models.DateField(default=timezone.now)
    passing_year = models.CharField(max_length=4, blank=True, null=True)

    def title(self):
        return 'Sir' if self.gender in self.GENDER[0] else 'Madam'

    def __str__(self) -> str:
            return f'{self.title()} {self.last_name  if  self.last_name else self.first_name}'
    
    def __repr__(self) -> str:
            return self.__str__()
    
    class Meta(CommonUser.Meta):
        abstract = True

# class LeaveReportStaff(models.Model):
#     staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE)
#     date = models.CharField(max_length=60)
#     message = models.TextField()
#     status = models.SmallIntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class NotificationStaff(models.Model):
#     staff = models.ForeignKey(StaffModel, on_delete=models.CASCADE)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
