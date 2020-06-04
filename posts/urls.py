from django.urls import path, re_path

from . import views


urlpatterns = [
    #path('test', views.user_list, name='user_list'),
    path('posts/', views.post_list, name='post_list'),
    #re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    #path('like/', views.like_post, name='like_post')
    re_path(r'^(?P<slug>[\w-]+)/like/$', views.PostLikeToggle.as_view(), name='like-toggle'),
    re_path(r'^api/(?P<slug>[\w-]+)/like/$', views.PostLikeAPIToggle.as_view(), name='like-api-toggle'),
    
   
    
    
]