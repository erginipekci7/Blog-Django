from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post
from .forms import PostForm

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})
    #return HttpResponse('post index sayfası')

def post_detail(request, id):
    #post = Post.objects.get(id=2)
    post = get_object_or_404(Post, id=id)
    context = {
        'post': post,
    }
    return render(request, 'post/detail.html', context)
    #return HttpResponse('post detail sayfası')
def post_create(request):
    """
    if request.method == 'POST':
        print(request.POST)
    """
    """
    title = request.POST.get('title')
    content = request.POST.get('content')
    Post.objects.create(title=title,content = content)
    """
    """
    if request.method == 'POST':
        #formdan gelen bilgileri kaydet
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        #formda göster
        form = PostForm()  # form nesnesi
    """
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form,
    }
    return render(request, 'post/form.html', context)

def post_update(request):
    return HttpResponse('post update sayfası')
def post_delete(request):
    return HttpResponse('post delete sayfası')