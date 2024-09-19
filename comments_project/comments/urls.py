from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include


app_name = 'comments'

urlpatterns = [
    path('', views.comment_list, name='comment_list'),
    path('add/', views.add_comment, name='add_comment'),
    path('admin/', admin.site.urls),
    path('comments/', include('comments.urls')),
]
