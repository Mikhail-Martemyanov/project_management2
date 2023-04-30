"""project_management2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from employee.views import EmployeeViewSet
from task.views import TaskViewSet

router = SimpleRouter()
router.register('employee', EmployeeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    # path('task/', include('task.urls')),

    path('task/', TaskViewSet.as_view({'get': 'list'}), name='task-list'),
    path('task/<int:pk>/', TaskViewSet.as_view({'get': 'retrieve'}), name='task-example'),
    path('task/<int:pk>/change_status/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='task-status'),
    path('task/<int:pk>/change_task/', TaskViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='task-change'),
    path('task/create_task/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='create-task'),
]
