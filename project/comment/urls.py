from django.conf.urls import url
from comment.views import comment

urlpatterns = [
    url(r'^(?P<commentID>\d+)/$', comment),
]