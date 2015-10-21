from django.shortcuts import render


def tableofcontents(request):
    return render(request, 'about.html')


def aboutme(request):
    return render(request, 'all_about_me.html')