from django.shortcuts import render

from .models import Post

# Create your views here.
def posts_list(request):
	posts = Post.objects.all()
	name = 'Alex'
	return render(request, 'blog/index.html', context={'posts':posts, 'name':name})

def post_detail(request, slug):
	post = Post.objects.get(slug__iexact = slug)
	return render(request, 'blog/post_detail.html', context = {'post': post})
