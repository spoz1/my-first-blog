#!coding:utf8
from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):   #всё, что мы получим от пользователя в качестве запроса через Интернет
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})#файл шаблона {} место, куда мы можем добавить что-нибудь для использования в шаблоне 
