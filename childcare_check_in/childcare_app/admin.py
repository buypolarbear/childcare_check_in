from django.contrib import admin
from childcare_app.models import Child, Profile, Check

admin.site.register([Child, Profile, Check])
