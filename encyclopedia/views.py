from django.shortcuts import render
from django.http import HttpResponse
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    """
    Get content of the encyclopedia entry per requierment 2
    """
    return render(request, "encyclopedia/title.html", {
        "title": util.get_entry(title)
    })
    #f = util.get_entry(title)
    #return HttpResponse(f)