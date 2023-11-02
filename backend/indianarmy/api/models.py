from django.db import models
from django.contrib.auth.models import AbstractUser


class TaskForce(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    is_active = models.BooleanField(default=True)
    overview = models.CharField(max_length=500, unique=True, null=False)
    requirements = models.CharField(max_length=250, unique=True, null=False)
    skills_you_will_learn = models.CharField(max_length=250, unique=True, null=False)

    CATEGORY = (
        ('MECHANICS & ENGINEERING', 'MECHANICS & ENGINEERING'),
        ('SCIENCE & MEDICINE', 'SCIENCE & MEDICINE'),
        ('SIGNAL & INTELLIGENCE', 'SIGNAL & INTELLIGENCE'),
        ('SUPPORT & LOGISTICS', 'SUPPORT & LOGISTICS'),
        ('GROUND FORCES', 'GROUND FORCES'),
        ('AVIATION & AERIAL DEFENCE', 'AVIATION & AERIAL DEFENCE'),
        ('NAVY FORCES', 'NAVY FORCES'),
    )
    category = models.CharField(max_length=100, choices=CATEGORY, null=False)

    only_for_soldiers = models.BooleanField(default=True)
    

class TaskForceApplication(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    applicant_email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    reason_for_application = models.CharField(max_length=500)
    recruiter_email = models.EmailField()

