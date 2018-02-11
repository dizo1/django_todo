from todos.views import TodoDelete, TodoUpdate

__author__ = 'Dunga'
from django.urls import path
from django.conf.urls import url
from todos.views import TodoUpdate, TodoDelete
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('todo/details/<todo_id>', views.details, name='detail'),
    path('add/', views.add, name='add'),
    #url(r'todo/(?P<pk>[0-9]+)/$', views.TodoUpdate.as_view(), name='update'),
    #url(r'todo/(?P<pk>[0-9]+)/delete/$', views.TodoDelete.as_view(), name='delete'),

    path('todo/<int:pk>/update/', TodoUpdate.as_view(), name='update'),
    path('todo/<int:pk>/delete/', TodoDelete.as_view(), name='delete'),

]
