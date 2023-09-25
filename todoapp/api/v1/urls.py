from . import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("tasks", views.TaskModelViewSet, basename="task")


urlpatterns = router.urls
