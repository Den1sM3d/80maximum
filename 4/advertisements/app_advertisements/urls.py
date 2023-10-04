from django.urls import path

from .views import example, top_sellers, advertisement_post

urlpatterns = [
    path("", example, name='main'),
    path("top-sellers/", top_sellers, name="top-sellers"),
    path("advertisement-post/", advertisement_post, name="advertisement-post"),
]