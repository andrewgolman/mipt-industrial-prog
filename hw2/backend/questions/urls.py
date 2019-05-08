from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('ask', views.AskView.as_view(), name='ask'),
    path('answer', views.AnswerView.as_view(), name='answer'),
    path('q<int:pk>', views.QuestionView.as_view(), name='question'),
    path('q<int:pk>/delete', views.DeleteQuestionView.as_view(), name='delete_question'),
]
