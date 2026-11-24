from django.views.generic import DetailView, ListView

from .models import Post


class PostList(ListView):
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLICADO)


class PostDetail(DetailView):
    template_name = "blog/post_detail.html"

    def get_queryset(self):
        return Post.objects.filter(status=Post.Status.PUBLICADO)