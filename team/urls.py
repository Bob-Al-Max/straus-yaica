from django.urls import path, re_path

from . import views

urlpatterns = [
    
    path('teams/', views.team_list, name='team_list'),
    re_path(r'^team/(?P<pk>\d+)/$', views.team_detail, name='team_detail'),
    re_path(r'^team-info/(?P<pk>\d+)/$', views.team_info, name='team_info'),
    re_path(r'^addpost/(?P<pk>\d+)/$', views.add_team_post, name='add_team_post'),
    
]