from django.contrib import admin

from workout_portal.models import Exercise, Training, SimpleUser
from workout_portal.models import models

# Register your models here.
admin.site.register(Exercise)
admin.site.register(Training)
admin.site.register(SimpleUser)
