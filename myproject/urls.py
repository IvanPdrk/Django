
from django.contrib import admin
from django.urls import path
from myproject import views as local_views
from posts import views as posts_views

urlpatterns = [
    path('hello-world/',local_views.hello_world),
    path('sorted/',local_views.sort),
    path('hi/<str:name>/<int:age>/',local_views.say_hi),
    path('posts/',posts_views.list_post)
]
