from django.db import models
from projects.models import Project
from users.models import Profile
from datetime import datetime


class ToDo (models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    assigned_to = models.ForeignKey(Profile, verbose_name='Assigned To', on_delete=models.PROTECT,
                                    related_name='assigned_to_profile')
    description = models.CharField(max_length=255, verbose_name='Description')
    created_by = models.ForeignKey(Profile, verbose_name='Created By', on_delete=models.PROTECT,
                                   related_name='created_by_profile'
                                   )
    create_date = models.DateField()
    plan_date = models.DateField()
    change_date = models.DateField()
    complete_date = models.DateField()
    is_done = models.BooleanField()


    def make_done(self):
        self.complete_date = datetime.now()
        self.is_done = True
        self.save()


    def save(self):
        self.change_date = datetime.now()
        super.save()
