from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home.html'),
    path('todos/', views.TodoList.as_view(), name='todos_list'),
    path('todos/<int:pk>/', views.TodoDetail.as_view(), name='todos_detail'),
    path('todos/add/', views.TodoCreate.as_view(), name='todos_add'),
    path('todos/<int:pk>/update/', views.TodoUpdate.as_view(), name='todos_update'),
    path('todos/<int:pk>/delete/', views.TodoDelete.as_view(), name='todos_delete'),
]