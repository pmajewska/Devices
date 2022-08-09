from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Urzadzenia, Laboratorium
from django.views.generic import ListView, DetailView, CreateView

def home(request):
    return render(request, 'home.html', {})


def index(request):
    laboratorium = Laboratorium.objects.all()
    dane = {'laboratorium': laboratorium}
    return render(request, 'szablon.html', dane)

def lab(request, id):
    lab_number = Laboratorium.objects.get(pk=id)
    lab_urzadzenie = Urzadzenia.objects.filter(Numer_laboratorium = lab_number)
    laboratorium = Laboratorium.objects.all()
    dane = {'lab_number': lab_number, 'lab_urzadzenie': lab_urzadzenie, 'laboratorium': laboratorium}
    return render(request, 'lab_urzadzenia.html', dane)

def dev(request, id):
    dev_number = Urzadzenia.objects.get(pk=id)
    laboratorium = Laboratorium.objects.all()
    dane = {'dev_number': dev_number, 'laboratorium': laboratorium}
    return render(request, 'urzadzenia.html', dane)

def post(request, id):
    post_number = Post.objects.get(pk=id)
    post = Post.objects.all()
    dane = {'post_number': post_number, 'post': post}
    return render(request, 'post.html', dane)

class PostListView(ListView):
    model = Post
    template_name = 'post.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class PostAddView(CreateView):
    model = Post
    template_name = 'post_add.html'
    fields = '__all__'

class PostView(ListView):
    model = Post
    template_name = 'home.html'

class SzablonView(ListView):
    model = Post
    template_name = 'szablon.html'