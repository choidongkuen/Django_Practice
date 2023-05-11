from django.contrib import admin

from pybo.models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ["subject"]
    fieldsets = [
        ('Subject Information', {'fields': ['subject']}),
        ('Content Information', {'fields': ['content']})
    ]


# Register your models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
