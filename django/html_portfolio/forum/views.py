from django.shortcuts import render


def forumfun(request):
    return render(request, 'Fake_Forum.html')