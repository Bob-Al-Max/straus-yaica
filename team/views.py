from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Team, Trophies
from posts.models import Posts

from main.models import Main
from users.models import CustomUser
from django.http import HttpResponseRedirect



def team_list(request):

    main = Main.objects.get(pk=1)
    teams = Team.objects.all()

    return render(request ,'team/team-list.html',{'main':main,'teams':teams})



def team_detail(request, pk):

    main = Main.objects.get(pk=1)
    team = Team.objects.get(pk=pk)
    #supporters = CustomUser.objects.filter(team=team)

    supporters = team.customuser_set.all()

    
   

    posts = Posts.objects.filter(author__pk__in = [s.pk for s in  supporters]).order_by('-created_at')

    return render(request ,'team/team-detail.html',{'main':main,'team':team,'posts':posts,'supporters':supporters})



def team_info(request, pk):
    main = Main.objects.get(pk=1)
    team = Team.objects.get(pk=pk)
    #supporters = CustomUser.objects.filter(team=team)
    trophies = team.trophies_set.all()

    supporters = team.customuser_set.all()

    posts = TeamPosts.objects.filter(team=pk).order_by('-created_at')

    return render(request ,'team/team-info.html',{'main':main,'team':team,'posts':posts,'supporters':supporters, 'trophies':trophies})




# def add_team_post(request):

#     author = CustomUser.objects.get(pk=1)
    

    
#     if request.method == 'POST':

#         title = request.POST.get('title')
#         content = request.POST.get('content')

#         upload_file = request.FILES['image']
#         fs = FileSystemStorage()

#         image = fs.save(upload_file.name, upload_file)
        

#         post = Posts(title=title, content=content, image=image)
#         post.author = author
        
#         post.save()

#         return redirect('team_detail', pk=pk)



#     return render(request ,'team/team-detail.html',{'team':team})


    
