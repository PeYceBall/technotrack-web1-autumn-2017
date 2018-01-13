from django.conf.urls import url
from core.views import profile
from core.views import UserDetail, signup
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^profile$', login_required(profile), name='profile'),
    url(r'^users/(?P<pk>\d+)', UserDetail.as_view(), name='user_detail'),
    url(r'^login/$', LoginView.as_view(template_name='login.html'), name="login"),
    url(r'^logout/$', login_required(LogoutView.as_view(template_name='logout.html')), name="logout"),
    url(r'^signup/$', signup, name="signup"),

]