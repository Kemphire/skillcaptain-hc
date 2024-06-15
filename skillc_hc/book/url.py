from django.urls import path
from . views import GenreList,BookDetail, AuthorDetail

urlpatterns = [
    path("genre/",GenreList.as_view(),name = "genre-list"),
    path("detail/<int:pk>",BookDetail.as_view(),name = "book-detail"),
    path("author/<int:pk>",AuthorDetail.as_view(),name = "author-detail")
]