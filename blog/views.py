
from django.http import HttpResponse, Http404
# from django.views.generic import CreateView
from django.shortcuts import redirect, render, get_object_or_404
from .models import Post
from .forms import PostForm, CommentForm

def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {'post_list': post_list,})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post,})

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
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


# post_new = CreateView.as_view(model=Post, form_class=PostForm)

def comment_new(request, post_pk):
    # try:
    #     post = Post.objects.get(pk=post_pk)
    # except Post.DoesNotExist:
    #     raise Http404
    # = 아래와 같다

    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            # 1. 필수값을 채우고자 할때
            # 2. 추가 세팅이 필요할때 v
            comment.post = post
            comment.save()
            return redirect(post)
    else:
        form = CommentForm()
    return render(request, 'blog/comment_form.html', {'form': form})

