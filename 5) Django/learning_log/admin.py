from django.contrib import admin

# Register your models here.

# topic import 
from .models import Topic
admin.site.register(Topic)

# entry import 
from .models import Entry
admin.site.register(Entry)