from django.contrib import admin
# from modeltranslation.admin import TranslationAdmin
from .models import Team, Portfolio, Testimonials, Stats, Xabar, Telegram
# Register your models here.

class XabarAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Email', 'Phone', 'Date', 'Checked')
    ordering = ('-User',)
    search_fields = ( 'User', 'Email')

admin.site.register(Xabar, XabarAdmin)
admin.site.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'position']

admin.site.register(Portfolio)
class PorrfolioAdmin(admin.ModelAdmin):

    list_display = ['title', 'desc']

admin.site.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['position', 'advice']


admin.site.register(Stats)
class StatsAdmin(admin.ModelAdmin):
    list_display = ['happy_clients']

class TelegramAdmin(admin.ModelAdmin):
    list_display = ('id', 'apiToken','chatID','Date')
    ordering = ('-id',)
    search_fields = ('id', 'Date')

admin.site.register(Telegram, TelegramAdmin)