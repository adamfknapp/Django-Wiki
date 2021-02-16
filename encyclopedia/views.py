from django.shortcuts import render
from django.http import HttpResponse
from . import util
#from django.http import QueryDict


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    """
    Get content of the encyclopedia entry per requierment 2
    """
    print('this is title')
    return render(request, "encyclopedia/title.html", {
        "title": util.get_entry(title)
    })

def search(request):
    query = request.GET.get('q')
    print('------' + str(query))
    return render(request, "encyclopedia/title.html", {
        "title": util.get_entry(title)
    })
