from django.contrib import admin
from django.urls import path, include
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', blog_views.latest_post, name='latest_post'),  # Root URL to latest_post
]