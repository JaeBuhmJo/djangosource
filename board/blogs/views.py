from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def post_list(request):
    posts = Post.objects.order_by("-created_at")
    return render(request, "blogs/post_list.html", {"posts":posts})

@login_required(login_url="users:login")
def post_create(request):
    if request.method =="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blog:post_list")
    else: 
        form = PostForm()
    return render(request,"blogs/post_write.html", {"form":form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id = post_id)

    is_liked = False

    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    context = {"post":post, "is_liked":is_liked}

    return render(request, "blogs/post_detail.html", context)

@login_required(login_url="users:login")
def post_edit(request, post_id):
    post=get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:post_detail", post.id)
    else:
        form = PostForm(instance=post)
    
    return render(request, "blogs/post_edit.html", {"form":form})

@login_required(login_url="users:login")
def post_delete(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.delete()
    return redirect("blog:post_list")

@login_required(login_url="users:login")
def post_like(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    is_liked=post.likes.filter(id=request.user.id).exists()

    is_liked_change = False

    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        is_liked_change = True
    return JsonResponse({"likes":post.likes.count(), "is_liked":is_liked_change})



