from django.shortcuts import render
from django import forms
from .models import Blog, Comment
from django.http import HttpResponse


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ("blog",)


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    return render(request, 'blog/blog.html', { 'blog': blog })

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/index.html', { 'blogs': blogs })

def comment(request, slug):
    blog = Blog.objects.get(slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.blog = blog
        comment.save()
    return render(request, 'blog/comment.html', { 'form': form, 'blog': blog })
