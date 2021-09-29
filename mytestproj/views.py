from django.shortcuts import render

def index(request):
    data = {
        'loc':'main'
    }

    return render(request,'pages/main.html', data)

def index_about(request):
    data = {
        'loc':'about'
    }

    return render(request,'pages/about.html', data)