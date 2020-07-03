from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Posts
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.files.storage import FileSystemStorage



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


@login_required
@require_POST
def image_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = Posts.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'}) 


@login_required
def add_post(request):
    from pytils.translit import slugify

    
    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        

        upload_file = request.FILES['image']
        fs = FileSystemStorage()

        image = fs.save(upload_file.name, upload_file)
        

        post = Posts(title=title, content=content, image= image)
        post.author = request.user
        post.slug = slugify(post.title.replace(" ", "-").lower())
        
        post.save()

        from django.http import HttpResponseRedirect

        #return redirect('user_detail', pk=request.user.pk)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



    return render(request ,'team/user_detail.html')      



          



             
                
            
                
        
            
               

