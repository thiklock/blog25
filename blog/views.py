from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})  # Directly 'post_detail.html'
def latest_post(request):
    try:
        latest_post = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date').first()
    except Post.DoesNotExist:
        latest_post = None
    return render(request, 'post_detail.html', {'post': latest_post})
def random_image_test(request):
    return render(request, 'random_image_test.html')