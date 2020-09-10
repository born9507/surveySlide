from django.contrib import admin

from .models import Survey

class SurveyAdmin(admin.ModelAdmin):
    fields = '__all__'

admin.site.register(Survey, )