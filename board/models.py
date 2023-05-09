from django.db import models


# Create your models here.
# 질문 ex) what is your hobby?
class Question(models.Model):
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.content


# 선택 ex) soccer,baseball ..

class Choice(models.Model):
    content = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Question 삭제시 Choice 삭제

    def __str__(self):
        return self.content
