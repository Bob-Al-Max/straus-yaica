from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from posts.models import Posts
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from posts.forms import PostCreateForm
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_POST
from common.decorators import ajax_required




def post_list(request):
    posts = Posts.objects.all()

    for post in posts:
        print(post.get_absolute_url())

    return render(request, 'posts/post-list.html',{'posts':posts})



def post_detail(request, slug=None):
    post = get_object_or_404(Posts, slug=slug)

    return render(request,'posts/post-detail.html',{'post':post})


class PostCreateView(CreateView):
    model = Posts
    fields = ['title','content','image']
    template_name = 'users/create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)
    




@login_required
def add_post(request):
    
    
    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        

        upload_file = request.FILES['image']
        

        post = Posts(title=title, content=content, image= upload_file)
        post.author = request.user
        
        
        post.save()

        from django.http import HttpResponseRedirect

        #return redirect(post.get_absolute_url())
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



    return render(request ,'users/user-detail2.html')  



@login_required
def post_create(request):
    if request.method == 'POST':
        # form is sent
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.author = request.user
            new_item.save()
            

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = PostCreateForm(data=request.GET)

    return render(request,
                  'users/user-detail2.html',
                  {
                   'form': form})


from posts.forms import ImageCreateForm

@login_required
def image_create(request):
    if request.method == 'POST':
        # form is sent
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            # form data is valid
            form.cleaned_data
            
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.author = request.user
            new_item.image = form.cleaned_data['image']
            
            new_item.save()
            

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)

    return render(request,
                  'posts/create.html',
                  {'section': 'images',
                   'form': form})


# @ajax_required
# @login_required
# @require_POST
# def post_like(request):
#     post_id = request.POST.get('id')
#     action = request.POST.get('action')
#     if post_id and action:
#         try:
#             post = Posts.objects.get(id=post_id)
#             if action == 'like':
#                 post.users_like.add(request.user)
#                 create_action(request.user, 'likes', post)
#             else:
#                 post.users_like.remove(request.user)
#             return JsonResponse({'status':'ok'})
#         except:
#             pass
#     return JsonResponse({'status':'ok'})                                             



          



             
                
            
                
        
            
               

