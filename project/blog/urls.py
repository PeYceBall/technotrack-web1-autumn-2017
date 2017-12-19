from django.conf.urls import url, include
from blog.views import blog
from blog.views import blogs_list
from blog.views import post
from blog.views import BlogDetail, BlogList, PostDetail

urlpatterns = [
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^(?P<pk>\d+)/$', BlogDetail.as_view(), name='blog_detail'),
    url(r'^[\d]+/(?P<pk>\d+)$', PostDetail.as_view(), name='post_detail'),
    #url(r'^[\d]+/comments/', include('comment.urls', namespace='comment')),
]

