from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

# 글 목록(게시판)을 보여줌.
def index(request):
    posts = Review.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'reviews/index.html', context)

# 글 작성 페이지 보여줌.
def new(request):
    return render(request, 'reviews/new.html')

# 글 작성 후 DB에 저장
def create(request):
    title_ = request.GET.get('title')
    content_ = request.GET.get('content')

    Review.objects.create(title=title_,content=content_)

    # 글 세부 페이지로 이동 (지금은 인덱스로)
    return redirect('reviews:index')

# 리뷰 보기 페이지
def detail(request, pk):
    post = Review.objects.get(id=pk)

    context = {
        'title': post.title,
        'content': post.content,
    }

    return render(request, 'reviews/detail.html', context)