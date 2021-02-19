from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from random import randint
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

class NewEntryForm(forms.Form):
    """
    Define form used to create new entry per requierment 11 of readme
    """
    title = forms.CharField(label="title")
    body = forms.CharField(label="body")

def new(request):
    """
    Create a new entry per requierment 11 of readme
    """
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })

def random(request):
    """
    Get a random page per requierment 20 of readme
    """
    entries = util.list_entries()
    n = randint(0,len(entries)-1)
    return render(request, "encyclopedia/title.html", {
            "title": util.get_entry(entries[n])
        })

def search(request):
    """
    Get contents of the search per requierments 7, 8, 9, 10
    """
    query = request.GET.get('q')
    results = util.search(query)

    #if an exact match open that entry
    if len(results) == 1:
        return render(request, "encyclopedia/title.html", {
            "title": util.get_entry(results[0])
        })
    #if multiple partial matches open list of options
    elif len(results) > 1:
        return render(request, "encyclopedia/search_results.html", {
            "entries": results
        })
    #else prompt user for new input
    else:
        return render(request, "encyclopedia/search_empty.html" 
        )