from django.db import models
from django.urls import reverse


class Question(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('question', kwargs={'pk': self.pk})

    def answers(self):
        return self.answer_set.order_by('id')


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('question', kwargs={'pk': self.question_id})

    def __str__(self):
        return self.text
