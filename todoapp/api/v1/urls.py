from . import views
from rest_framework.routers import DefaultRouter
from django.urls import path

app_name = "api-v1"

router = DefaultRouter()
router.register("tasks", views.TaskModelViewSet, basename="task")


urlpatterns =[
             path("weather/", views.GetWeatherApiView().as_view(), name="weather"),
] 
urlpatterns+=router.urls

