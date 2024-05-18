from django.shortcuts import render

from website.models import CustomFile


def index(request):
    return render(request, 'website/index.html')


def photo_gallery(request):
    photos = CustomFile.objects.all()
    return render(request, 'website/photos.html', {'photos': photos})
