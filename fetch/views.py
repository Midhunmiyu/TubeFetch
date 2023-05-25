
from django.contrib import messages
from django.shortcuts import render, redirect
from pytube import YouTube
from tqdm import tqdm
import time


def index(request):
    if request.method == 'POST':
        link = request.POST['link'].strip()
        video = YouTube(link)
        stream = video.streams.get_lowest_resolution()
        stream.download('D:\\python\\TubeFetch\\Saved_video')
        pbar = tqdm(total=100)
        for i in range(10):
            time.sleep(0.3)
            pbar.update(10)
        pbar.close()
        messages.info(request, 'Video Downloaded Successfully...!!')
        return render(request,'index.html')
    return render(request, 'index.html')
