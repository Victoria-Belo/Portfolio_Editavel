from django.contrib import admin
from app.models import About, Team, Feature, Note


@admin.register(About)
class aboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'about', 'icon_select')


@admin.register(Feature)
class featureAdmin(admin.ModelAdmin):
    list_display = ('title', 'about', 'icon_select')


@admin.register(Team)
class teamAdmin(admin.ModelAdmin):
    list_display = ('name', 'office', 'photo')


@admin.register(Note)
class noteAdmin(admin.ModelAdmin):
    list_display = ('title', 'note')