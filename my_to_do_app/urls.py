from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createTodo, name='createTodo'),
    path('delete/', views.deleteTodo, name='deleteTodo'),
    path('update/', views.updateTodo, name='updateTodo'),
]