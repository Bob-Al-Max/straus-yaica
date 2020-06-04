from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .models import Team, TeamPosts

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
    supporters = CustomUser.objects.filter(team=team)

   

    posts = TeamPosts.objects.filter(team=pk).order_by('-created_at')

    return render(request ,'team/team-detail.html',{'main':main,'team':team,'posts':posts,'supporters':supporters})


def add_team_post(request, pk):

    author = CustomUser.objects.get(pk=1)
    team = Team.objects.get(pk=pk)

    
    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')

        upload_file = request.FILES['image']
        fs = FileSystemStorage()

        image = fs.save(upload_file.name, upload_file)
        

        post = TeamPosts(title=title, content=content, image=image)
        post.author = author
        post.team = team
        post.save()

        return redirect('team_detail', pk=pk)



    return render(request ,'team/team-detail.html',{'team':team})


    