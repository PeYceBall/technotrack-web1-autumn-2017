from django.conf.urls import url
from like.views import like
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<blog_id>\d+)/(?P<pk>\d+)/like$', login_required(like), name='like'),
]