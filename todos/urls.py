from todos.views import TodoDelete, TodoUpdate

__author__ = 'Dunga'
from django.urls import path
from django.conf.urls import url, include
from todos.views import TodoUpdate, TodoDelete
from django.contrib.auth import views as auth_views
from . import views
from todos import views as core_views




urlpatterns = [
    path('', views.index, name='index'),
    path('todo/details/<todo_id>', views.details, name='detail'),
    path('add/', views.add, name='add'),
    url(r'^signup/$', core_views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^login/$', auth_views.login, name='login'),
    #url(r'^logout/$', auth_views.logout, name='logout'),
    #url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    #url(r'todo/(?P<pk>[0-9]+)/$', views.TodoUpdate.as_view(), name='update'),
    #url(r'todo/(?P<pk>[0-9]+)/delete/$', views.TodoDelete.as_view(), name='delete'),

    path('todo/<int:pk>/update/', TodoUpdate.as_view(), name='update'),
    path('todo/<int:pk>/delete/', TodoDelete.as_view(), name='delete'),

]
