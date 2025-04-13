from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('latest/', views.latest_post, name='latest_post'),
    path('random-image-test/', views.random_image_test, name='random_image_test'), # Add this line
]