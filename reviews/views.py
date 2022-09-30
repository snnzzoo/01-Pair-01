from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    return render(request, 'reviews/index.html')

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