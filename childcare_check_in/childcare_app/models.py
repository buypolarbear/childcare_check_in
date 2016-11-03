from django.db import models



ACCESS_LEVEL = [
    ('p', 'Parent'),
    ('s', 'Staff')
]

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=TYPE)


class Child(models.Model):
    first_name = models.CharField(max_length="15")
    last_name = models.CharField(max_length="25")
    parent = models.ForeignKey('auth.User')
    on_site = models.BooleanField(default=False)
    check_in = models.DateTimeField(auto_now=True)
    check_out = models.DateTimeField(auto_now=True)


class Pin(models.Model):
    child = models.OneToOneField(Child)
    number = models.IntegerField()
