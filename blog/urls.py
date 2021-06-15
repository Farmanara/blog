from django.urls import path
from .views import index,post,category

app_name="blog"
urlpatterns = [
    path('',index,name="index"),
    path('detail/<slug:slug>',post,name="post"),
    path('category/<slug:slug>',category,name="category")

]