from django.urls import path
from .views import PostListCreateView, PostDetailView, CommentListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]

# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register(r'posts', views.PostListCreateView, basename='post-list-create')  # CRUD for Post
# router.register(r'posts/<int:pk>/', views.PostDetailView, basename='post-detail')
# router.register(r'posts/(?P<post_id>\d+)/comments', views.CommentListCreateView, basename='comment')  # Comments under each Post

# # urlpatterns = [
# #     # Add any additional app-specific URLs here
# # ]

# urlpatterns += router.urls

