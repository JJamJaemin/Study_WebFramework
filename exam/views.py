from django.shortcuts import render
from .models import Student #모델을 가져오고 그 안에 있는 Post클래스 가져오기
from django.views.generic import ListView, DetailView # 장고가 가지고 있는 클래스들 리스트를 볼수 있고 하나하나 볼수있는 페이지
# Create your views here.

#CBV 방식
# class PostList(ListView):
#     model = Student #자동적으로 post_list로 저장 따라서 view파일에 posts를 쓴것을 바꿔줘야함
#     template_name = 'exam/index.html'  #템플릿 지정 (지정안하면 post_list로 자동지정)

def index(request):
    return render(
        request,
        'exam/index.html',
    )
class St_List(ListView):
    model = Student #자동적으로 post_list로 저장 따라서 view파일에 posts를 쓴것을 바꿔줘야함
    template_name = 'exam/st_list.html' #템플릿 지정 (지정안하면 post_list로 자동지정)
    ordering = '-pk' #오름차순, 내림차순 지정

class St_Detail(ListView):
    model = Student #자동적으로 post_list로 저장 따라서 view파일에 posts를 쓴것을 바꿔줘야함
    template_name = 'exam/st_card.html' #템플릿 지정 (지정안하면 post_list로 자동지정)
    ordering = '-pk' #오름차순, 내림차순 지정

#FBV 방식
#def index(request):
#    posts = Post.objects.all().order_by('-pk')#Post.object.all은 데이터 베이스 안에있는 모든것들을 가져오기
                                             #order_by(-pk)는 역순으로 가져오기 -가 안붙으면 순서대로

    #여기서의 posts의미는 모든 게시글을 의미
#    return render(
#        request,
#        'blog/index.html',
#        {#중괄호 안에 의미는 html에 넘겨줄 데이터가 있을때 중괄호 사용
#            'posts': posts,
            #변수  : 데이터 형태를 가짐
#        }
#    )

#class를 이용한 방식
# class PostDetail(DetailView):
#     model = Post
#     template_name = 'blog/single_post_page.html'

#함수를 이용한 방식
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk) #pk값은 현재 pk값을 가져와라 라는 의미
#     return render(
#         request,
#         'blog/single_post_page.html',
#         {#html에 post변수를 넘겨준다
#             'post' : post,
#         }
#     )