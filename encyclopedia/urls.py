from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<str:name>/",views.entry,name="entry"),
    path("newPage/",views.newPage,name="newPage"),
    path("search/",views.search,name="search"),
    path("randomPage/",views.randomPage,name="randomPage"),
]
