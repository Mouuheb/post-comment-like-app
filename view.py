from django.shortcuts import render, redirect
from .models import Post, Comment, Like

def add_comment(request, post_id):
    if request.method == 'POST':
        user = request.user
        comment_text = request.POST.get('comment_text')
        post = Post.objects.get(id=post_id)
        new_comment = Comment(user=user, post=post, content=comment_text)
        new_comment.save()
    return redirect('post_detail', post_id=post_id)

def add_like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    
    # Check if the user has already liked the post to prevent duplicate likes
    existing_like = Like.objects.filter(user=user, post=post).first()
    if not existing_like:
        new_like = Like(user=user, post=post)
        new_like.save()
    
    return redirect('post_detail', post_id=post_id)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    likes = Like.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'likes': likes})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    likes = Like.objects.filter(post=post)
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'likes': likes})
