from django.urls import path, re_path

from . import views



urlpatterns = [
    
    path('like/', views.post_like, name='like'),
    path('users/follow/', views.user_follow, name='user_follow'),
    path('users/', views.user_list, name='user_list'),
    re_path(r'^user/(?P<pk>\d+)/$', views.user_detail, name='user_detail'),
    path('signup/', views.app_signup, name="app_signup"),
   
    #path('user/addpost/', views.add_post, name="add_post"),
    #path('user-class/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
    re_path(r'^user-update/(?P<pk>\d+)/$', views.UserUpdate.as_view(), name='user-update'),
    
     
    
    

    
    
    
    

  
   
]
