from django.shortcuts import render
from .models import Post #모델을 가져오고 그 안에 있는 Post클래스 가져오기
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')#Post.object.all은 데이터 베이스 안에있는 모든것들을 가져오기
                                             #order_by(-pk)는 역순으로 가져오기 -가 안붙으면 순서대로

    #여기서의 posts의미는 모든 게시글을 의미
    return render(
        request,
        'blog/index.html',
        {#중괄호 안에 의미는 html에 넘겨줄 데이터가 있을때 중괄호 사용
            'posts': posts,
            #변수  : 데이터 형태를 가짐
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) #pk값은 현재 pk값을 가져와라 라는 의미
    return render(
        request,
        'blog/single_post_page.html',
        {#html에 post변수를 넘겨준다
            'post' : post,
        }
    )