from django.shortcuts import render
from .models import Category
from .models import Post
from .models import Comment


def blog_index(request):
    category = Category.objects.all()
    post = Post.objects.all()
    comment = Comment.objects.all()
    context = {
        'category': category,
        'post': post,
        'comment': comment
    }
    return render(request, 'blog_index.html', context)


def blog_details(request, pk):
    category = Category.objects.get(pk=pk)
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.get(pk=pk)
    context = {
        'category': category,
        'post': post,
        'comment': comment
    }
    return render(request, 'blog_details.html', context)