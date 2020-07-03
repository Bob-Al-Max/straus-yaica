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



          



             
                
            
                
        
            
               

