from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Blog, Comment
from .forms import BlogForm, CommentForm


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_app/blog_list.html'
    context_object_name = 'blogs'



class BlogCreateView(LoginRequiredMixin, View):
    template_name = 'blog/blog_form.html'

    def get(self, request):
        form = BlogForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog-list')
        return render(request, self.template_name, {'form': form})



class BlogUpdateView(LoginRequiredMixin, View):
    template_name = 'blog/blog_form.html'

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if not (request.user.is_superuser or blog.author == request.user):
            return redirect('blog-list')
        form = BlogForm(instance=blog)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if not (request.user.is_superuser or blog.author == request.user):
            return redirect('blog-list')
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog-list')
        return render(request, self.template_name, {'form': form})



class BlogDeleteView(LoginRequiredMixin, View):
    template_name = 'blog/blog_confirm_delete.html'

    def get(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if not request.user.is_superuser:
            return redirect('blog-list')
        return render(request, self.template_name, {'object': blog})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        if not request.user.is_superuser:
            return redirect('blog-list')
        blog.delete()
        return redirect('blog-list')



class AddCommentView(LoginRequiredMixin, View):
    template_name = 'blog/comment_form.html'

    def get(self, request, pk):
        form = CommentForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        blog = get_object_or_404(Blog, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = blog
            comment.user = request.user
            comment.save()
            return redirect('blog-list')
        return render(request, self.template_name, {'form': form})
