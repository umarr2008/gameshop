from django.contrib import admin
from .models import Game

class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'release_date', 'genre', 'image_display']
    list_filter = ['release_date', 'genre']
    search_fields = ['title', 'genre', 'description']
    date_hierarchy = 'release_date'
    readonly_fields = ['image_display']

    def image_display(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "No Image"
    image_display.allow_tags = True
    image_display.short_description = 'Preview'

admin.site.register(Game, GameAdmin)
