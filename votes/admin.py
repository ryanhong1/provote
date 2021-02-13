from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Question)
class Questionadmin(admin.ModelAdmin):
    """Custom Question Admin """

    list_display = (
        "question_text",
        "pub_date",


    )

@admin.register(models.Choice)
class Choiceadmin(admin.ModelAdmin):
    """Custom Question Admin """

    list_display = (
        "choice_text",
        "votes",
        "question",


    )

