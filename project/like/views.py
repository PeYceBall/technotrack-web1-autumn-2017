# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from like.models import Like
from django.core.urlresolvers import reverse
from blog.models import Post
from blog.views import PostDetail

# Create your views here.


def like(request, blog_id, pk):
    like = Like()
    like.post = Post.objects.all().filter(pk=pk)[0]
    like.user = request.user
    like_query_set = Like.objects.filter(user=like.user, post=like.post)
    if like_query_set.count():
        like_query_set.delete()
    else:
        like.save()

    return redirect('blog:post_detail', blog_id=blog_id, pk=pk)
