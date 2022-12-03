from django.shortcuts import render
from . import util
from django.http import HttpResponse
import random


def index(request):
    if(len(request.GET.dict()) == 2):
        title = request.GET.get('title')
        content = request.GET.get('content')
        print('title:',title,'content:',content)
        util.save_entry(title,content)
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "selected":'CSS'
        })
    elif(len(request.GET.dict()) == 0):
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "selected":'CSS'
        })
    else:
        return HttpResponse(404)

def entry(request,name):
    print(type(util.get_entry(name)))
    response = render(request,"encyclopedia/detail.html",{
        'thing':name,
        'file':util.get_entry(name)
    })
    response["Access-Control-Allow-Origin"] = '*'
    return response

def newPage(request):
    return render(request,"encyclopedia/newPage.html")

def search(request):
    searchTitle = request.GET.get('q')
    titles = util.list_entries()
    newTitles = [title for title in titles if title == searchTitle]
    return render(request, "encyclopedia/search.html", {
        "entries":newTitles,
        'titleLenth':newTitles.__len__
    })

def randomPage(request):
    return render(request,"encyclopedia/randomPage.html",{
        'selected':random.sample(util.list_entries(),1)
    })



