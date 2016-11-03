from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


ACCESS_LEVEL = [
    ('p', 'Parent'),
    ('s', 'Staff')
]

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance, access_level='p')


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVEL)


class Child(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    parent = models.ForeignKey('auth.User')
    on_site = models.BooleanField(default=False)
    check_in = models.DateTimeField(auto_now=True)
    check_out = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=4, unique=True)
