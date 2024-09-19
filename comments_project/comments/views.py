from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Comment
from django.http import JsonResponse
from django.template.loader import render_to_string

def preview_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # Створюємо попередній перегляд коментаря
            preview_content = render_to_string('comments/preview_template.html', {
                'comment': form.cleaned_data
            })
            return JsonResponse({'preview': preview_content})
        else:
            return JsonResponse({'error': 'Невірні дані'}, status=400)
    return JsonResponse({'error': 'Неправильний метод'}, status=400)


def add_comment(request, parent_id=None):
    parent_comment = None
    if parent_id:
        parent_comment = get_object_or_404(Comment, id=parent_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent = parent_comment
            comment.save()
            return redirect('comments:comment_list')
    else:
        form = CommentForm(initial={'parent': parent_comment})

    return render(request, 'comments/add_comment.html', {'form': form, 'parent_comment': parent_comment})

def comment_list(request):
    comments = Comment.objects.filter(parent__isnull=True).order_by('-created_at')  # Тільки головні коментарі
    return render(request, 'comments/comment_list.html', {'comments': comments})

def preview_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            # Створюємо попередній перегляд коментаря
            preview_content = render_to_string('comments/preview_template.html', {
                'comment': form.cleaned_data
            })
            return JsonResponse({'preview': preview_content})
        else:
            return JsonResponse({'error': 'Невірні дані'}, status=400)
    return JsonResponse({'error': 'Неправильний метод'}, status=400)
