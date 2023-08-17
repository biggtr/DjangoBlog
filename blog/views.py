from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):  # new
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post
    fields = ["title", "author", "body"]
    template_name = "post_new.html"
    success_url = "/"


class BlogUpdateView(UpdateView):
    model = Post
    fields = ["title", "body"]
    template_name = "post_update.html"
    success_url = "/"


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
    context_object_name = "post"
