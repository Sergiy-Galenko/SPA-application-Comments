from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('add/', views.add_comment, name='add_comment'),
    path('add/<int:parent_id>/', views.add_comment, name='reply_comment'),
    path('preview/', views.preview_comment, name='preview_comment'),  # Маршрут для попереднього перегляду
]
