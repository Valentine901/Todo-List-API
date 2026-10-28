from rest_framework import serializers
from .models import TodoList
from user.serializers import UserResponseSerializer


class CreateTodoList(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ["title", "description"]

class TodoListResponse(serializers.ModelSerializer):
    user = UserResponseSerializer()
    class Meta:
        model = TodoList 
        fields = ["id", "title", "description", "mark_completed", "created_at", "updated_at", "user"]

class UpdateTodoList(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ["title", "description", "mark_completed"]
