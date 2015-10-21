from django.shortcuts import render

# Create your views here.
def javapicindex(request):
    return render(request, 'index.html')

def javapicjoin(request):
    return render(request, 'join.html')


def javapicgallery(request):
    return render(request, 'gallery.html')