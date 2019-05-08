from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.shortcuts import redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


class IndexView(ListView):
    model = Question
    template_name = 'index.html'

    def get_queryset(self):
        return Question.objects.order_by('-id')


class QuestionView(DetailView):
    model = Question
    template_name = 'question.html'

    def get_form(self):
        return AnswerForm(initial={'question': self.kwargs['pk']})


class AnswerView(CreateView):
    model = Answer
    form_class = AnswerForm

    def get(self, request):
        return redirect('/')


class AskView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'ask.html'


class DeleteQuestionView(DeleteView):
    model = Question
    success_url = reverse_lazy('index')
