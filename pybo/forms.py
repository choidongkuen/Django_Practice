from django import forms

from pybo.models import Question


class QuestionFrom(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
