from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name='질문 내용')
    pub_date = models.DateTimeField(auto_now_add= True, verbose_name='질문 생성 시각')
    description = models.TextField(verbose_name='설명', null=True)
    
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField(max_length=200, verbose_name='보기 내용')
    votes = models.IntegerField(default = 0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text     