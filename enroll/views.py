# from django.shortcuts import render
# from .models import Video

# # Create your views here.


# def upload_video(request):
#     if request.method == 'POST':
#         title = request.POST['title']
#         video_file = request.FILES['video_file']
#         Video.objects.create(title=title, video_file=video_file)
#     return render(request, 'upload.html')

# def watch_video(request, video_id):
#     video = Video.objects.get(id=video_id)
#     return render(request, 'watch.html', {'video': video})
