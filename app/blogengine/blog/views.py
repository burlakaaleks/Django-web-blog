from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import get_object_or_404

from .models import *
from .utils import ObjectDetailMixin

# Create your views here.
def posts_list(request):
	posts = Post.objects.all()
	name = 'Alex'
	return render(request, 'blog/index.html', context={'posts':posts, 'name':name})

# def post_detail(request, slug):
# 	post = Post.objects.get(slug__iexact = slug)
# 	return render(request, 'blog/post_detail.html', context = {'post': post})

class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_detail.html'
	# def get(self, request, slug):
	# 	# post = Post.objects.get(slug__iexact = slug)
	#
	# 	post = get_object_or_404(Post, slug__iexact = slug)
	# 	return render(request, 'blog/post_detail.html', context = {'post': post})

class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'
	# def get(self, request, slug):
	# 	tag = Tag.objects.get(slug__iexact=slug)
	# 	return render(request, 'blog/tag_detail.html', context={'tag':tag})

def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags':tags})

# def tag_detail(request, slug):
# 	tag = Tag.objects.get(slug__iexact=slug)
# 	return render(request, 'blog/tag_detail.html', context={'tag':tag})
