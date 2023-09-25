from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import DefaultPagination
from .filters import TaskFilter
from ...models import Task


class TaskModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    pagination_class = DefaultPagination
    filterset_class = TaskFilter
    search_fields = ["title"] 
    ordering_fields = ["created_date"]


