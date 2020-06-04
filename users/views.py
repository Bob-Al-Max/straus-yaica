from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from users.models import CustomUser
from django.contrib.auth import login, authenticate, logout
from django.core.files.storage import FileSystemStorage
from main.models import Main
from posts.models import Posts
from django.views.generic import RedirectView

from team.models import Team


from .forms import CustomUserCreationForm


def user_list(request):

    users = CustomUser.objects.all()

    context = {'users':users}

    return render(request, 'users/user_list.html', context)



def user_detail(request, pk):

    main = Main.objects.get(pk=1)
    user = CustomUser.objects.get(pk=pk)
    posts = user.posts_set.all().order_by('-created_at')
    supporters = CustomUser.objects.filter(team = user.team)
    context = {'user':user, 'posts':posts, 'main':main,'supporters':supporters}

    return render(request, 'users/user_detail.html', context)



   




# def post_like(request,pk):

#     if request.method == 'POST':

#         user = request.user
#         post = Posts.objects.get(title='New York')

#         like = PostLike(user=user,post=post)
#         like.save()


#     return HttpResponse('like')

        






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




def test(request):

    return HttpResponse("test") 



def app_login(request):

    if request.method == 'POST' :

        email = request.POST.get('email')
        password = request.POST.get('password')

        if email != "" and password != "" :

            user = authenticate(email=email, password=password)

            if user != None :
                login(request, user)
                return redirect('home')

    return render(request, 'users/auth.html')            



def app_logout(request):

    logout(request)

    return redirect('app_login')


    


            

            
                    

          
