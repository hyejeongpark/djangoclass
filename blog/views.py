from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def add(request, x, y):
    # return HttpResponse(str(int(x) + int(y)))
    return render(request, 'blog/add.html', {
        'x': x,
        'y': y,
        'result': int(x) + int(y),
        })

def hello(request, name):
    return HttpResponse('hello %s' % name)

def archives(request, year, month, day):
    return HttpResponse('%s년 %s월 %s일' % (year, month, day))