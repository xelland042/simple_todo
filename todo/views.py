from rest_framework import viewsets
from todo.models import Todo
from todo.serializers import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend


class TodoModelViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_done', 'created_at', 'updated_at']
