from django.contrib import admin
from .models import Survey, Question, Choice, Result, Answer

pages_models = [Survey, Question, Choice, Result, Answer]
admin.site.register(pages_models)