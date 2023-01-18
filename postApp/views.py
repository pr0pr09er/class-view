from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Author, Publisher
from .forms import PostForm


# Create your views here.
def default():
    if Category.objects.all().count() == 0:
        Category.objects.all().create(name='Ужасы')
    if Author.objects.all().count() == 0:
        Author.objects.all().create(name='Sasha', age=17)
    if Publisher.objects.all().count() == 0:
        Publisher.objects.all().create(name='OOO Books', boss='Sergey')


class PostView(ListView):
    default()
    model = Post
    template_name = 'postApp/home.html'
    context_object_name = 'posts'


class DeletePost(DeleteView):
    model = Post
    template_name = 'postApp/delete.html'

    def get_success_url(self):
        return reverse('home')


class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'postApp/edit.html'

    def get_success_url(self):
        return reverse('home')


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'postApp/add.html'

    def get_success_url(self):
        return reverse('home')
