from rest_framework import viewsets, views, response
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
import requests
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
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



class GetWeatherApiView(views.APIView):
    @method_decorator(cache_page(60*20))
    @method_decorator(vary_on_cookie)
    def get(self, request, *args, **kwargs):
        response=requests.get("https://api.openweathermap.org/data/2.5/weather?lat=34.6422939&lon=50.8801184&appid=36066caa84bc7ebf1aaebf15af72ee6d")     
        return Response(response.json())