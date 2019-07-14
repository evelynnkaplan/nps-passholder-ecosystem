from django.db import models
from datetime import date

class Passholder(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'

class Pass(models.Model):
  STANDARD = 'Standard'
  SENIOR_LIFETIME = 'Senior Lifetime'
  SENIOR_ANNUAL = 'Senior Annual'
  ACCESS = 'Access'
  MILITARY = 'Military'
  GRADE_4 = '4th Grade'
  VOLUNTEER = 'Volunteer'
  PASS_TYPES = (
    (STANDARD, 'Annual Pass'),
    (SENIOR_LIFETIME, 'Senior Lifetime Pass'),
    (SENIOR_ANNUAL, 'Senior Annual Pass'),
    (ACCESS, 'Access Pass'),
    (MILITARY, 'US Military'),
    (GRADE_4, 'Annual 4th Grade Pass'),
    (VOLUNTEER, 'Volunteer Pass')
  )
  passholder_primary = models.ForeignKey(
    Passholder,
    on_delete=models.SET_NULL,
    null=True
    )
  passholder_secondary = models.CharField(max_length=200, null=True, blank=True)
  type = models.CharField(
    max_length=30,
    choices=PASS_TYPES,
    default=STANDARD,
  )
  expiration_date = models.DateField('Expiration date', null=True)
  zip_code = models.IntegerField(null=True)
  email = models.EmailField(max_length=100)
  phone_num = models.CharField(max_length=20)
  cost = models.DecimalField(max_digits=5, decimal_places=2)
  
  def __str__(self):
    return f'{self.type}'

  class Meta:
    verbose_name_plural = "passes"

class Park(models.Model):
  name = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  zip_code = models.IntegerField

  def __str__(self):
    return f'{self.name}'

class Visit(models.Model):
  passholder = models.ForeignKey(
    Passholder,
    on_delete=models.SET_NULL,
    blank=True, 
    null=True
    )
  date = models.DateField
  park = models.ForeignKey(Park, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.passholder.first_name} {self.passholder.last_name}, {self.park}, {self.date}"

