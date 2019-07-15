from django.db import models
from datetime import date

class Passholder(models.Model):
  first_name = models.CharField(max_length=200)
  last_name = models.CharField(max_length=200)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'

  def passes(self):
    passes = []
    passes_set = self.pass_set.all()
    for pass_item in passes_set:
      passes.append(pass_item)
    
    return passes

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
    related_name='passes',
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    default=[]
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

  def valid(self):
    today = date.today()
    return today <= self.expiration_date
  valid.boolean = True
  
  def __str__(self):
    return f"{self.type}, ID: {self.id}, Valid: {self.valid()}, Expiration: {self.expiration_date}"

  class Meta:
    verbose_name_plural = "passes"

class Park(models.Model):
  name = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  zip_code = models.IntegerField(null=True)

  def __str__(self):
    return f'{self.name}'

class Visit(models.Model):
  passholder = models.ForeignKey(
    Passholder,
    related_name="visits",
    on_delete=models.SET_NULL,
    blank=True, 
    null=True,
    default=[]
    )
  date = models.DateField(null=True)
  park = models.ForeignKey(Park, related_name='visits', on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.passholder.first_name} {self.passholder.last_name}, {self.park}, {self.date}"

