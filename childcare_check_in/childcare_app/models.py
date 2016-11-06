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

    @property
    def all_checks(self):
        return Check.objects.all()

    @property
    def all_children(self):
        if self.access_level == 'p':
            return Child.objects.filter(parent=self.user)
        return Child.objects.all()

    @property
    def all_payments(self):
        all_children = self.all_children
        total = sum(child.total_payment for child in all_children)
        return total

class Child(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    parent = models.ForeignKey('auth.User')
    code = models.CharField(max_length=4, unique=True)

    @property
    def all_checks(self):
        return Check.objects.filter(child=self)

    @property
    def total_time(self):
        all_checks = self.all_checks
        total = sum(check.daily_time.seconds for check in all_checks)
        return round(total / 3600, 3)

    @property
    def total_payment(self):
        total_time = self.total_time
        hourly_rate = 1000.00
        return round(float(total_time * hourly_rate), 2)


class Check(models.Model):
    child = models.ForeignKey(Child)
    on_site = models.BooleanField(default=False)
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(auto_now=False, null=True)

    class Meta:
        ordering = ["-id"]

    @property
    def daily_time(self):
        return self.time_out - self.time_in
