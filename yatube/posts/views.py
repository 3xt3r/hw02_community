from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from yatube.settings import NUMBER_OF_POSTS


def index(request):
    posts = Post.objects.order_by('-pub_date')[:NUMBER_OF_POSTS]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(
        Group.objects.all().prefetch_related('posts'),
        slug=slug)
    posts = group.posts.all()[:NUMBER_OF_POSTS]

    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
