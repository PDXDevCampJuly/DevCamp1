from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    content = {"someadjective": 'Awesome',
               "somename": 'Summer'
              }
    return render(request, 'index.html', content)

def corgisareawesome(request):
    return HttpResponse("Corgis are awesome! <a href='./'>Homepage!</a>")


def forum(request):
    return render(request, 'Fake_Forum.html')