import re
import markdown2
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseNotFound


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


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    Assumes title is in MD and returns html.
    See Requierment 1 in read me. 
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        f = f.read().decode("utf-8")
        return markdown2.markdown(f)
    except FileNotFoundError:
        return HttpResponseNotFound("<h1>Page NOT found</h1>")
