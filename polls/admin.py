from django.contrib import admin
from .models import Question, Choice

# Register your models here.


# admin.site.register(Choice)

class ChoiceInline(admin.ModelAdmin):
    model = Choice
    extra = 2
    # inlines = [ChoiceInline]

class QuestionAdmin(admin.ModelAdmin):
    fieldSets = [
        (None, {'fields': ['q']}),
        # ('Date Information', {'fields': ['pub_ate'], })
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, ChoiceInline)

