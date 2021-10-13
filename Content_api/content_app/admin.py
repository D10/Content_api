from django.contrib import admin

from .models import Page, VideoContent, AudioContent, TextContent, Content


class VideoContentAdmin(admin.StackedInline):
    model = VideoContent
    extra = 0


class AudioContentAdmin(admin.StackedInline):
    model = AudioContent
    extra = 0


class TextContentAdmin(admin.StackedInline):
    model = TextContent
    extra = 0


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )
    list_display_links = ('id', 'title', )
    list_filter = ('title', )
    search_fields = ('title', 'content__title')
    save_on_top = True

    inlines = [VideoContentAdmin, AudioContentAdmin, TextContentAdmin]
