from django.http import HttpResponse
from django.shortcuts import render


def hello(request, nome):
    return render(request, 'index.html', {'nome': nome})


def articles(request, id):
    return HttpResponse(f"Article {id}")
