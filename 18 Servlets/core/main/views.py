from django.shortcuts import render
from PIL import Image

# Create your views here.
from main.models import Photo
from .utils import change_photo


def photoPageView(request):

    if request.method == 'GET':
        path = change_photo()
        objects_list = {'photo':path}
        return render(request, 'main.html', objects_list)