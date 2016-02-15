from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def post_lists(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	#Please note that we create a variable for our QuerySet: posts. 
	#Treat this as the name of our QuerySet. From now on we can refer to it by this name.
	return render(request,'blog/post_list.html',{'posts':posts})
