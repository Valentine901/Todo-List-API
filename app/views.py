from rest_framework.response import Response
from rest_framework import status 
from rest_framework.views import APIView
from .serializers import CreateTodoList, TodoListResponse, UpdateTodoList
from rest_framework.permissions import  IsAuthenticated
from .models import TodoList
from django.shortcuts import get_object_or_404


class AddTodoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = CreateTodoList(data=request.data)
        serializer.is_valid(raise_exception=True)
        # save() returns an object
        todo = serializer.save(user=request.user)
        return Response(TodoListResponse(todo).data, status=status.HTTP_201_CREATED)


class TodoDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is None:
            todo_list = TodoList.objects.filter(user=request.user)
            return Response(TodoListResponse(todo_list, many=True).data, status=status.HTTP_200_OK)
        else:
            todo = get_object_or_404(TodoList, id=pk, user=request.user)
            return Response(TodoListResponse(todo).data, status=status.HTTP_200_OK)

    def get_todo(self, request, pk):
        todo = get_object_or_404(TodoList, pk, user=request.user)
        return todo
    
    def put(self, request, pk):
        todo = self.get_todo(request=request, pk=pk)
        serializer = UpdateTodoList(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        return Response(TodoListResponse(todo).data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        todo = self.get_todo(request=request, pk=pk)
        serializer = UpdateTodoList(todo, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        updated_todo = serializer.save()
        return Response(TodoListResponse(updated_todo).data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        todo = self.get_todo(request, pk)
        todo.delete()
        return Response({"message":"Todo list deleted successfully"}, status=status.HTTP_204_NO_CONTENT)