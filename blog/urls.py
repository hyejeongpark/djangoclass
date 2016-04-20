from django.conf.urls import url
import blog.views

urlpatterns = [
    url(r'^$', blog.views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', blog.views.post_detail, name='post_detail'),
    url(r'^new/$', blog.views.post_new, name='post_new'),
]