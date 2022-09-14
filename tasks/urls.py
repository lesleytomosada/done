from django.urls import path
from .views import TaskCreateView, SelfTaskListView

urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path("mine/", SelfTaskListView.as_view(), name="show_my_tasks"),
]
