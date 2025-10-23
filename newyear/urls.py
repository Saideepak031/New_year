from django.urls import path
from . import views

app_name = 'newyear'
urlpatterns = [
    path('', views.index, name='index'),
    path('note/delete/<int:pk>/', views.delete_note, name='delete_note'),
    path('goal/toggle/<int:pk>/', views.toggle_goal, name='toggle_goal'),
]