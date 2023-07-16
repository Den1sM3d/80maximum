from django.urls import path
from .views import ls4_homework_response

urlpatterns = [
    path('', ls4_homework_response),
    path('lesson_4/', ls4_homework_response)
]
