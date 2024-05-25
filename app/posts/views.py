from django.shortcuts import render
from .models import Post, Comment, Like
from users.models import Profile


# Create your views here.

# post list
def PostViews(request):
    qs=Post.objects.all()
    try:
        user=Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        print("error")
    if request.method=="POST":
        p_form=Post
    return render(request, "post/post.html", {})

# post create 
def PostCreateViews(request):
    return render(request, "post/post.html", {})

# post update 
def PostUpdateViews(request):
    return render(request, "post/post.html", {})


# post delete 
def PostDelateViews(request):
    return render(request, "post/post.html", {})