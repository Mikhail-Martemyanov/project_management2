from django.urls import path, include
from rest_framework.routers import SimpleRouter

from task.views import TaskViewSet

router = SimpleRouter()
router.register('', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
