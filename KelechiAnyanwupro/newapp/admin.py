from django.contrib import admin

# Register your models here.
from .models import Church, School

admin.site.register(Church)
admin.site.register(School)