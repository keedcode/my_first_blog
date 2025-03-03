from django.shortcuts import render
from django.utils import timezone

# Include the model we have written in models.py
from .models import Post
# Create your views here.
def post_list(request):
    # This is a variable for our queryset
    posts = Post.objects.filter(published_at__lte=timezone.now()).order_by('published_at')
    return render(request, 'blog/post_list.html', {'posts':posts})