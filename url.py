from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('add_like/<int:post_id>/', views.add_like, name='add_like'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    # ...
]
