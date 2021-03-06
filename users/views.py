from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from users.models import CustomUser
from django.contrib.auth import login, authenticate, logout
from django.core.files.storage import FileSystemStorage
from main.models import Main
from posts.models import Posts
from django.views.generic import RedirectView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.edit import UpdateView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Contact
from django.contrib.auth.decorators import login_required




from team.models import Team


from .forms import CustomUserCreationForm

@login_required
def user_list(request):

    users = CustomUser.objects.all()

    context = {'users':users}

    return render(request, 'users/user_list.html', context)



    
    

def user_detail(request, pk):

    main = Main.objects.get(pk=1)
    user = CustomUser.objects.get(pk=pk,is_active=True)
    posts = user.posts_set.all().order_by('-created_at')
    paginator = Paginator(posts, 2)

    page = request.GET.get('page')

    supporters = CustomUser.objects.filter(team = user.team)
    

    try:
        posts = paginator.page(page)
        context = {'section': 'people','user':user, 'posts':posts, 'main':main,'supporters':supporters}

    except PageNotAnInteger:
        # Если переданная страница не является числом, возвращаем первую.
        posts = paginator.page(1)
        context = {'section': 'people','user':user, 'posts':posts, 'main':main,'supporters':supporters}

    except EmptyPage:
        if request.is_ajax():
            # Если получили AJAX-запрос с номером страницы, большим, чем их количество,
            # возвращаем пустую страницу.
            return HttpResponse('')

        posts = paginator.page(paginator.num_pages) 
        context = {'section': 'people','user':user, 'posts':posts, 'main':main,'supporters':supporters}

    if request.is_ajax():
        return render(request, 'users/posts_ajax.html', context)

    return render(request, 'users/user-detail2.html', context)    






@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = CustomUser.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,
                                              user_to=user)
                
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except CustomUser.DoesNotExist:
            return JsonResponse({'status':'ok'})
    return JsonResponse({'status':'ok'})    


# class UserDetailView(DetailView,MultipleObjectMixin):
#     model = CustomUser
#     template_name = 'users/user-detail2.html'
#     context_object_name = "user"
#     paginate_by = 5
    

#     def get_object(self):
#         id_ = self.kwargs.get('id')
#         return get_object_or_404(CustomUser, id=id_)


#     def get_context_data(self, **kwargs):
        
#         object_list = Posts.objects.filter(author=self.get_object())
#         #posts = self.object.posts_set.all().order_by('-created_at')
#         context = super(UserDetailView, self).get_context_data(object_list=object_list,**kwargs)
#         #context['posts'] = self.object.posts_set.all().order_by('-created_at')

        
#         context['main'] = Main.objects.get(pk=1)
#         context['supporters'] = CustomUser.objects.filter(team = self.object.team)
        
        
#         return context






class UserUpdate(UpdateView):
    model = CustomUser
    fields = ['team','profile_img']
    template_name_suffix = '_update_form'            


            
 
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

        return redirect('user_detail', pk=request.user.pk)



    return render(request ,'team/user_detail.html')    








def app_signup(request):

    main = Main.objects.get(pk=1)
    
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(request, user)
        return redirect('home')
    
    return render(request, 'users/signup.html', {'form': form, 'main':main})



def user_wall(request,pk):
    return render(request,'users/user_wall.html', {})




@ajax_required
@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = Posts.objects.get(id=post_id)
            if action == 'like':
                post.users_like.add(request.user)
                create_action(request.user, 'likes', post)
            else:
                post.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ok'})    



    





                      



    




            






                    





    


            

            
                    

          
