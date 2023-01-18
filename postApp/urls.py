from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.PostView.as_view(), name='home'),
    path('home/delete/<int:pk>/', views.DeletePost.as_view(), name='delete'),
    path('home/edit/<int:pk>/', views.UpdatePost.as_view(), name='edit'),
    path('home/create/', views.CreatePost.as_view(), name='create'),
]
