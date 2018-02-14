from django.shortcuts import render,HttpResponse
from .models import Post

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})
    #return HttpResponse('post index sayfası')

def post_detail(request):
    return HttpResponse('post detail sayfası')
def post_create(request):
    return HttpResponse('post create sayfası')
def post_update(request):
    return HttpResponse('post update sayfası')
def post_delete(request):
    return HttpResponse(request)