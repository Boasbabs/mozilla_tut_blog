from django.shortcuts import render


def index(request):
    return render(request, "story/index.html", context={})