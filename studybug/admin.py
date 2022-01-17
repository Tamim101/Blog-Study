from django.contrib import admin

# Register your models here.
from studybug.models import *

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)