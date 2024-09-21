from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Comment
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

class CommentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        comments = Comment.objects.filter(parent__isnull=True).order_by('-created_at')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    # Отримуємо параметри пошуку та сортування з GET-запиту
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', '-created_at')  # За замовчуванням сортуємо за датою (нові спочатку)

    # Якщо є пошуковий запит, фільтруємо всі коментарі (включно з вкладеними)
    if query:
        comment_list = Comment.objects.filter(
            Q(username__icontains=query) | Q(text__icontains=query)
        ).order_by(sort_by)
    else:
        # Якщо пошуку немає, відображаємо тільки головні коментарі
        comment_list = Comment.objects.filter(parent__isnull=True).order_by(sort_by)

    # Пагінація: 5 коментарів на сторінку
    paginator = Paginator(comment_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'comments/comment_list.html', {'page_obj': page_obj, 'query': query, 'sort_by': sort_by})

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
