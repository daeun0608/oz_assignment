from django.contrib import admin
from django.urls import path
from feeds import views

urlpatterns = [
    path("", views.show_feed),
    path("all", views.all_feed),
    path("<int:feed_id>/<str:feed_content>", views.one_feed)
]