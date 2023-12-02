from django.urls import path
from .views import Task_List, Task_Detail, Task_Create


urlpatterns = [
    path('', Task_List.as_view(), name="tasks"),
    path('task/<int:pk>/', Task_Detail.as_view(), name='task'),
    path('task-create/', Task_Create.as_view(), name='task-create')
]