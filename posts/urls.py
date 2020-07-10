from django.urls import path, re_path

from . import views





urlpatterns = [
    path('like/', views.post_like, name='like'),
    #path('create/', views.PostCreateView.as_view(), name='create'),
    path('create/', views.image_create, name='create'),
    path('user/addpost/', views.add_post, name="add_post"),
    #path('user/post_create/', views.post_create, name="post_create"),
    
    path('posts/', views.post_list, name='post_list'),
    #re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #re_path(r'^(?P<id>[\d-]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^user-posts/(?P<pk>\d+)/$', views.user_posts, name='user_posts'),
    re_path(r'^user-posts-detail/(?P<pk>\d+)/$', views.user_post_detail, name='user_post_detail'),
    
    
    
    
   
    
    
]