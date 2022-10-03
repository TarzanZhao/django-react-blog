# from django.conf.urls import url
from django.urls import include, re_path
from .views import PostList, PostCreate, PostRetrieveUpdateDestroy
from .views import TagListCreate, TagRetrieveUpdateDestroy

from .feeds import MainFeed
from .activities import posts_stream

urlpatterns = [
    # List posts
    re_path(r'^posts/$', PostList.as_view(), name='post_list'),
    # List posts filtered by tag
    re_path(r'^tag/(?P<tag>[^\.]+)/$', PostList.as_view()),
    re_path(r'^category/(?P<category>[^\.]+)/$', PostList.as_view()),

    # Create post
    re_path(r'^post/new$', PostCreate.as_view(), name='post_create'),

    # Retreive/Update/Delete Post
    re_path(r'post/(?P<slug>[^\.]+)/$',
        PostRetrieveUpdateDestroy.as_view(),
        name='post_detail'),

    re_path(r'^tags/$', TagListCreate.as_view(), name='tag_list'),    
    re_path(r'tag/(?P<slug>[^\.]+)/$', TagRetrieveUpdateDestroy.as_view(), name='tag_detail'),

    # Atom Feed
    re_path(r'^feed/rss$', MainFeed()),
    # Activities
    re_path(r'^feed/posts/new$', posts_stream),
    
]

app_name = 'posts'