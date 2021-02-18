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

def search(request):
    """
    Get contents of the search per requierments 7, 8, 9, 10
    """
    query = request.GET.get('q')
    results = util.search(query)

    #if an exact match return open that entry
    if len(results) == 1:
        return render(request, "encyclopedia/title.html", {
            "title": util.get_entry(results[0])
        })
    #if multiple partial matches open list of options
    elif len(results) > 1:
        return render(request, "encyclopedia/search_results.html", {
            "entries": results
        })
    else:
        return render(request, "encyclopedia/search_empty.html" 
        )