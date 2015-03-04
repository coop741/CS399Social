from django.contrib import admin
from .models.mood import Mood


class MoodAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mood, MoodAdmin)
