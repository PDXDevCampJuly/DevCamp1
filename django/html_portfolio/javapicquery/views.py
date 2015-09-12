from django.shortcuts import render
from django.http import HttpResponse


def javapicqueryindex(request):
    return render(request, 'indexjq.html')


def javapicqueryjoin(request):
    return render(request, 'joinjq.html')


def javapicquerygallery(request):
    return render(request, 'galleryjq.html')