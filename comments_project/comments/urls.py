from django.urls import path
from . import views
from .views import CommentListCreateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'comments'

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('add/', views.add_comment, name='add_comment'),
    path('add/<int:parent_id>/', views.add_comment, name='reply_comment'),
    path('preview/', views.preview_comment, name='preview_comment'),  # Маршрут для попереднього перегляду
    path('api/comments/', CommentListCreateAPIView.as_view(), name='comment_api'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
