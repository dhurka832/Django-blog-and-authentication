from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts':posts
    }
    return render(request, "index.html",context)

def detail_post(request,id):
    post = Post.objects.get(pk=id)
    context = {
        'post':post
    }
    return render(request, "post_detail.html",context)

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            user.save()
            messages.success(request, "The post has been created successfully")
            return redirect("posts")
        else:
            messages.error(request, "Please correct the following errors")
    else:
        form = PostForm()
    return render(request, "post_form.html",{'form':form})

@login_required
def update_post(request,id):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "The post has been updated successfully")
            return redirect("posts")
    else:
        form = PostForm(instance=post)
    return render(request, "update_post.html",{'form':form})

@login_required
def delete_post(request,id):
    post = Post.objects.get(pk=id)
    if request.method == "POST":
        post.delete()
        messages.success(request, "The post has been deleted successfully")
        return redirect("posts")
    return render(request, "post_confirm_delete.html")
    
