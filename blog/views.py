from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list,})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post,})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            # 방법 1)
            # url = reverse('blog:post_detail', args=[post.pk])
            # return redirect(url)

            # 방법 2)
            # return redirect(post.get_absolute_url())

            # 방법 3)
            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form,})