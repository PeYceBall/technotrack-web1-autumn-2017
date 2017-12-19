from django.conf.urls import url
from core.views import profile
from core.views import UserDetail

urlpatterns = [
    url(r'^profile$', profile, name='profile'),
    url(r'^users/(?P<pk>\d+)', UserDetail.as_view(), name='user_detail')
]