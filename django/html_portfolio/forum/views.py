from django.shortcuts import render
from django.http import HttpResponse


def index(request):

    return render(request, 'index.html')

def aboutme(request):
    return render(request, 'all_about_me.html')

def javapicprettiness(request):
    return render(request, 'join.html')
    #return HttpResponse('join.html')
    #   < a href = './' > Homepage! < / a > "

def jqueriness(request):
    return render(request, 'joinjq.html')


def zen_mockery(request):
    return render(request, 'zen_mockup.html')


def forumfun(request):
    return render(request, 'Fake_Forum.html')