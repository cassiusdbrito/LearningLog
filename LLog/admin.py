from django.contrib import admin
from LLog.models import Topic, Entry

admin.site.register([Topic, Entry])