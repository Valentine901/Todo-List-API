from django.urls import path 
from .views import AddTodoView, TodoDetails

urlpatterns = [
    path("create-todo/", AddTodoView.as_view()),
    path("todos/", TodoDetails.as_view()),
    path("todos/<int:pk>/", TodoDetails.as_view())
]