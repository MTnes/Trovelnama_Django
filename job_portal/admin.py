from django.contrib import admin
from .models import *

@admin.register(Team_Members)
class Team_memberAdmin(admin.ModelAdmin):
    pass

@admin.register(Blogs)
class BlogAdmin(admin.ModelAdmin):
    pass