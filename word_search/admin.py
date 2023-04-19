from django.contrib import admin
from . models import Word

# Register your models here.

@admin.register(Word)
class WordsAdmin(admin.ModelAdmin):
    list_display=['id', 'first_form', 'second_form', 'third_form']
