import re
import markdown2
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseNotFound


def clean_title(text):
    return re.sub('[^A-Za-z0-9]+', '', text).strip().lower()


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title, return_html=True):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    Assumes title is in MD and returns html.
    See Requierment 1 in read me.
    """
    try:
        # Per requierment 1, 2s of Readme
        f = default_storage.open(f"entries/{title}.md")
        f = f.read().decode("utf-8")
        if return_html:
            return markdown2.markdown(f)
        else:
            return f
    except FileNotFoundError:
        # Per requirement 3 of Readme
        return "<h1>Page not found</h1>"


def search(query):
    """
    Accepts a string query and returns a list of matches
    See Requierment 7, 8, 9, 10 in read me.
    """

    # Standardize query and entries. Strip query of special characters.
    query = clean_title(query)
    entries = [x.strip().lower() for x in list_entries()]

    # search for exact matches per requierment 8
    if query in entries:
        return [query]
    # Search for partial matches per requierment 9
    elif query in '\t'.join(entries):
        return [x for x in entries if query in x]
    # return an empty list if no matches
    else:
        return []
