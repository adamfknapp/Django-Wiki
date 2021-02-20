from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from random import randint
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_title(request, title):
    """
    Get content of the encyclopedia entry per requierment 2
    """
    return render(request, "encyclopedia/title.html", {
        "title_name": title
        ,"title": util.get_entry(title)
    })


class NewEntryForm(forms.Form):
    """
    Define form used to create new entry per requierment 11 of readme
    """
    title = forms.CharField( max_length=50, required=True)
    content = forms.CharField(widget= forms.Textarea, max_length=1000, required=True)

def new(request):
    """
    Handle a new entry per requierment 11 of readme
    """
    #Listen for a POST request and process data when detected
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = util.clean_title(form.cleaned_data['title'])
            content = form.cleaned_data['content']
           
            #concatenate title to content for consistent display
            # ------>   Start here -----> content = f{'newtext ->' {content} }

            #If the title is unique per requierment 14 in readme
            if title not in util.list_entries():
                util.save_entry(title, content) 
                #direct user to newly created page per requierment 15 of readme
                return get_title(request, title)
            else:
                return render(request, "encyclopedia/error.html" )
        
    #Else create a blank form
    else:
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