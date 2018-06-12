from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from . models import Video



@login_required(login_url="/accounts/login")
def home(request):
    latest_video = Video.objects.latest('date_posted')
    context = {'latest_video' : latest_video}
    return render(request, 'videos/home.html', context)

@login_required(login_url="/accounts/login")
def watch(request, video_id):
    video = Video.objects.get(pk=video_id)
    context = {'video' : video}
    return render(request, 'videos/watch.html', context)
    

@login_required(login_url="/accounts/login")
def library(request):
    video_list = Video.objects.all()

    videos = Paginator(video_list, 3)

    grouped_videos = []
    for page in videos.page_range:
        page_objects = videos.page(page).object_list
        grouped_videos.append(page_objects)

    context = {'videos' : videos, 'grouped_videos' : grouped_videos}
    return render(request, 'videos/library.html', context)