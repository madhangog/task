from django.conf.urls import url
from . import views
from django.urls import path
from django.contrib.sitemaps.views import sitemap
# from blog.sitemaps import PostSitemap
# from .feeds import LatestPostsFeed


urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    url(r'^$', views.post_list, name='post_list'),
    path('post/<int:post_id>', views.view_post, name='view_post'),
#  url(r'^(?P<post_id>\d+)$', views.post_share,name='post_share'),
#  url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
#  url(r'^feed/$', LatestPostsFeed(), name='post_feed')

]
