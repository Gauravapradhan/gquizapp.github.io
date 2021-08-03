from django.contrib import admin
from django.urls import path
from .views import(QuizListView,
    quiz_view,
    quiz_data_view,
    save_view)
app_name='quizz'
urlpatterns = [
    path('', QuizListView.as_view(),name='main-view'),
    path('<pk>/',quiz_view,name='quiz-view'),
    path('<pk>/data/',quiz_data_view,name='quiz-data-view'),
    path('<pk>/save/',save_view,name='save-view'),
]