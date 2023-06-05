from django.shortcuts import render
from .forms import *
import os
from django.conf import settings
from .recognition import recognition_img as rimg


def image_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            name_file = os.path.join(settings.MEDIA_ROOT, r"images\\", str(request.FILES['img']))
            data_recognized = rimg(name_file)
            os.remove(name_file)
            return render(request, 'results.html', {'data_recognized': data_recognized})
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
