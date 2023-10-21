from django.db import models
from apps.users.models import StaffModel
from django.utils.translation import gettext_lazy as _

class Hostel(models.Model):
    name = models.CharField(_('Name'), max_length=20)
    no = models.CharField(_('Room Number'), max_length=10)
    ty = models.CharField(_('Room Type'), max_length=10)
    n_bed = models.PositiveSmallIntegerField(_('Number of bed'))
    students = models.ManyToManyField('student.Student', related_name='hostel')

    @property
    def number_of_students(self):
        return self.students.objects.count()
    
    class Meta:
        verbose_name = _("hostel")
        verbose_name_plural = _("hostels")
        db_table = _('hostels')

class FundRaising(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    earnings = models.PositiveSmallIntegerField(_('earning'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("fund_raising")
        verbose_name_plural = _("fund_raisings")
        db_table = _('fund_raisings')

class Driver(StaffModel):
    driver_license = models.CharField(_('license'), max_length=20)
    class Meta:
        verbose_name = _("driver")
        verbose_name_plural = _("drivers")
        db_table = _('drivers')

class Vehicle(models.Model):
    route = models.CharField(_('route'), max_length=20)
    no = models.CharField(_('Number'), max_length=20)
    driver = models.OneToOneField(Driver, blank=True, null=True, on_delete=models.SET_NULL)

    def driver_license(self):
        return self.driver.driver_license

    class Meta:
        verbose_name = _("vehicle")
        verbose_name_plural = _("vehicles")
        db_table = _('vehicles')
