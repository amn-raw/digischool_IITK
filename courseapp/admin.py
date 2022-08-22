import imp
from django.contrib import admin
from courseapp.models import CLASS_COURSES_MAPPING
from courseapp.models import AVAILABLE_COURSES
from courseapp.models import ALL_ANOUNCEMENT
# Register your models here.

admin.site.register(CLASS_COURSES_MAPPING)
admin.site.register(AVAILABLE_COURSES)
admin.site.register(ALL_ANOUNCEMENT)
