from django.urls import path, include
from django.conf.urls import url
from .views import todoListView

urlpatterns = [
    url(r'^list/all/$', todoListView, name="todo-listview"),
]
