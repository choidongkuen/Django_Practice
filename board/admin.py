from django.contrib import admin

from board.models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['content']}),
        ('Date Information', {'fields': ['created_at']})
    ]
    inlines = [ChoiceInline]  # Questions 테이블 에서 Choice 항목 같이 보기
    list_display = ('content', 'created_at')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
