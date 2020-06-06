from django.contrib import admin
from .models import Form,Hospital,Doctor,Time
# Register your models here.


admin.site.register(Hospital)
admin.site.register(Form)
admin.site.register(Doctor)
admin.site.register(Time)