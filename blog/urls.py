from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.blog_index, name='blog_index'),
    url(r'^(?P<post_id>[0-9]+)/$', views.post_detail, name = 'post_text'),
    url(r'^test', views.develop, name='test'),
]