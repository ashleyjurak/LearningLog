from django.contrib import admin

# Register your models here.

from .models import Topic #. means to look in same directory structure as where admin file is
from .models import Entry

admin.site.register(Topic)
admin.site.register(Entry)