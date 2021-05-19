from django.db import models
from users.models import Profile
from datetime import datetime


class ProjectMember (models.Model):
    member_profile = models.ForeignKey(Profile, verbose_name="Member")
    MANAGER = 'MANAGER'
    MEMBER = 'MEMBER'
    MEMBER_ROLES = [
        (MANAGER, 'Project Manager')
        (MEMBER, 'Project Member')
    ]
    member_role = models.CharField(max_length=8, choices=MEMBER_ROLES, default=MEMBER)


class Project (models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True, blank=False, verbose_name='Project Name')
    repo_link = models.URLField(verbose_name='Repository URL-link')
    change_date = models.DateField(verbose_name='Change Date')
    DRAFT = 'DRAFT'
    ACTIVE = 'ACTIVE'
    CLOSED = 'CLOSED'
    STATUS_LIST = [
        (DRAFT, 'Draft'),
        (ACTIVE, 'Active'),
        (CLOSED, 'Closed'),
    ]
    status = models.CharField(max_length=8, blank=False, choices=STATUS_LIST, default=DRAFT,
                              verbose_name='Project Status')
    project_members = models.ManyToOneRel(ProjectMember)


    def save(self, *args, **kwargs):
        self.change_date = datetime.now()
        super().save(*args, **kwargs)


    def activate_project(self):
        self.status = self.ACTIVE
        self.save()

