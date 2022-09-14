from django.urls import path
from .views import TaskCompletionUpdateView, TaskCreateView, SelfTaskListView

urlpatterns = [
    path("create/", TaskCreateView.as_view(), name="create_task"),
    path(
        "<int:pk>/complete/",
        TaskCompletionUpdateView.as_view(),
        name="complete_task",
    ),
    path("mine/", SelfTaskListView.as_view(), name="show_my_tasks"),
]
