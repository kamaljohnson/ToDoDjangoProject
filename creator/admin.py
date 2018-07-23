from django.contrib import admin
from .models import Snippet, Tags, Status

admin.site.register(Snippet)
admin.site.register(Tags)
admin.site.register(Status)
