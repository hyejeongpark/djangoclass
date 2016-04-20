from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'blog.views.index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^new/$', 'blog.views.post_new'),
]