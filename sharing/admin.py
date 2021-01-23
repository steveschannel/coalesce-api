from django.contrib import admin
from .models import Tag
from .models import Item

admin.site.register(Tag)
admin.site.register(Item)