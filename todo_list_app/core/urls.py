from django.urls import path
from .views import Task_List, Task_Detail, Task_Create, Task_Update, Task_Delete, Custom_Login, Signup_Page
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', Task_List.as_view(), name="tasks"),
    path('task/<int:pk>/', Task_Detail.as_view(), name='task'),
    path('task-create/', Task_Create.as_view(), name='task-create'),
    path('task-update/<int:pk>/', Task_Update.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', Task_Delete.as_view(), name='task-delete'),
    path('login/', Custom_Login.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page = 'login'), name="logout"),
    path('signup/', Signup_Page.as_view(), name='signup')
]