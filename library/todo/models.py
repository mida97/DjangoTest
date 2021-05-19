from django.db import models
from projects.models import Project
from users.models import Profile
from datetime import datetime


class ToDo (models.Model):
    todo_id = models.AutoField()
    project = models.ForeignKey(Project)
    assigned_to = models.ForeignKey(Profile, verbose_name='Assigned To')
    description = models.CharField(max_length=255, verbose_name='Description')
    created_by = models.ForeignKey(Profile, verbose_name='Created By')
    create_date = models.DateField()
    plan_date = models.DateField()
    change_date = models.DateField()
    complete_date = models.DateField()
    is_done = models.BooleanField()


    def make_done(self):
        self.complete_date = datetime.now()
        self.change_date = datetime.now()
        self.is_done = True
        self.save()


    def save(self):
        self.change_date = datetime.now()
        super.save()
