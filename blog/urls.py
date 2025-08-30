from django.urls import path
from .views import (
    BlogListView, BlogCreateView, BlogUpdateView, BlogDeleteView, AddCommentView
)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('create/', BlogCreateView.as_view(), name='blog-create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='blog-update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog-delete'),
    path('comment/<int:pk>/', AddCommentView.as_view(), name='add-comment'),
]


