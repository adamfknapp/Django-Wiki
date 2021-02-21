from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index")
    , path("wiki/<str:title>", views.get_title, name="title")
    , path("edit/<str:title_name>",views.edit,name="edit")
    , path("search/",views.search,name="search")
    , path("random/",views.random,name="random")
    , path("new/",views.new,name="new")
]
