import imp
from django.contrib import admin
from loginapp.models import USER_SIGNUP_DATABASE
from loginapp.models import QUERY_DATABASE
from loginapp.models import OTP_DATABASE
from loginapp.models import TEACHER_CODE_MAPPING
# Register your models here.
admin.site.register(USER_SIGNUP_DATABASE)
admin.site.register(QUERY_DATABASE)
admin.site.register(OTP_DATABASE)
admin.site.register(TEACHER_CODE_MAPPING)
