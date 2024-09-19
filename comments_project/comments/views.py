from django.shortcuts import render, redirect
from .forms import CommentForm
from .models import Comment

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments:comment_list')
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form})

def comment_list(request):
    comments = Comment.objects.all().order_by('-created_at')
    return render(request, 'comments/comment_list.html', {'comments': comments})
