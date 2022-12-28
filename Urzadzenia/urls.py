from django.urls import path
#from . import view
from .views import *

urlpatterns = [
    #path('', views.home, name="home"),
    path('', PostView.as_view(), name="home"),
    path('post/', PostListView.as_view(), name='post'),
    path('wpis/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', PostAddView.as_view(), name='add_post'),

    path('lab/', LabView.as_view(), name='lab'),
    path('lab/<id>/', lab, name='laby'),
    path('dev/<id>/', dev, name='dev'),
    path('lab/<int:pk>', LabDetailView.as_view(), name='lab_detail'),
    #path('post/<id>/', post, name='post')
]