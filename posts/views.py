from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Posts
from django.views.generic import RedirectView



def post_list(request):
    posts = Posts.objects.all()

    for post in posts:
        print(post.get_absolute_url())

    return render(request, 'posts/post-list.html',{'posts':posts})



def post_detail(request, slug=None):
    post = get_object_or_404(Posts, slug=slug)

    return render(request,'posts/post-detail.html',{'post':post})


def like_post(request):
    post = get_object_or_404(Posts, id=request.POST.get('id'))
    post.likes.add(request.user)

    print(post)

    return HttpResponseRedirect(post.get_absolute_url())


class PostLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        slug = self.kwargs.get("slug")
        print(slug)
        post = get_object_or_404(Posts, slug=slug)
        url_ = post.get_absolute_url()
        user = self.request.user
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)

        print(post)        
        return url_    



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions



class PostLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        # slug = self.kwargs.get("slug")
        post = get_object_or_404(Posts, slug=slug)
        url_ = post.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user in post.likes.all():
            liked = False
            post.likes.remove(user)
                
        else:
            liked = True
            post.likes.add(user)
                
        updated = True
        counts=post.likes.count()
        data = {
            "updated": updated,
            "liked": liked,
            "likescount": counts,
        }
        return Response(data)


  



          



             
                
            
                
        
            
               

