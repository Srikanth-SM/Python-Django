from django.db import models

# Create your models here.


class Question(models.Model):
    question_text = models.CharField('question text', max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return "{},{}".format(self.question_text, self.pub_date)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField("choice text", max_length=200)
    votes = models.IntegerField("votes", default=0)

    def __str__(self):
        return "{}".format(self.choice_text)
    


