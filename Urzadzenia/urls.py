from django.urls import path
#from . import views
from .views import PostListView, PostDetailView, PostAddView, PostView, SzablonView
from .views import *

urlpatterns = [
    #path('', views.home, name="home"),
    path('', PostView.as_view(), name="home"),
    path('post/', PostListView.as_view(), name='post'),
    path('wpis/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', PostAddView.as_view(), name='add_post'),

    path('szablon/', SzablonView.as_view(), name='szablon'),
    path('lab/<id>/', lab, name='lab'),
    path('dev/<id>/', dev, name='dev'),
    #path('post/<id>/', post, name='post')
]