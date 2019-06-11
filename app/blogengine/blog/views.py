from django.shortcuts import render

# Create your views here.
def posts_list(request):
	n = 'Alex'
	labels = ['Nike', 'Adidas', 'Virginia', 'Marlboro']
	return render(request, 'blog/index.html', context={'labels':labels, 'name':n})