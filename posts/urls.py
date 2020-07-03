from django.urls import path, re_path

from . import views




urlpatterns = [
    path('user/addpost/', views.add_post, name="add_post"),
    path('posts/', views.post_list, name='post_list'),
    #re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='post_detail'),
    
    
    
   
    
    
]