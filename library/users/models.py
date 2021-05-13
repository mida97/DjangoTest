from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save


class User(AbstractUser):
    email = models.EmailField(max_length=64, unique=True, verbose_name='email address', blank=False)
    test_name = models.CharField(verbose_name='test name', max_length=150, blank=True)


    def save(self, *args, **kwargs):
        if self.__new__():
            self.set_password(raw_password='init123')
        super().save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        #instance.set_password(raw_password='init123')
        #instance.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
