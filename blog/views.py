from django.shortcuts import render, redirect
from .models import Post,Category,Tag #모델을 가져오고 그 안에 있는 Post클래스 가져오기
from django.views.generic import ListView, DetailView,CreateView # 장고가 가지고 있는 클래스들 리스트를 볼수 있고 하나하나 볼수있는 페이지
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

#CBV 방식
class PostList(ListView):
    model = Post #자동적으로 post_list로 저장 따라서 view파일에 posts를 쓴것을 바꿔줘야함
    #template_name = 'blog/index.html' #템플릿 지정 (지정안하면 post_list로 자동지정)
    ordering = '-pk' #오름차순, 내림차순 지정

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data() #post_list를 가져옴
        context['categories'] = Category.objects.all() #Category db의 내용을 가져옴 #context를 추가 안할시 기본적으로 post_list를 가져옴
        context['no_category_post_count'] = Post.objects.filter(category=None).count()#카테고리가 분류되어있지 않은 경우(미분류 갯수)
        return context # -> post_list.html

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
class PostDetail(DetailView):
    model = Post
    # template_name = 'blog/single_post_page.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data() #post_list를 가져옴
        context['categories'] = Category.objects.all() #Category db의 내용을 가져옴
        context['no_category_post_count'] = Post.objects.filter(category=None).count()#카테고리가 분류되어있지 않은 경우(미분류 갯수)
        return context # -> post_detail.html (post, categories, no_category_post_count)것들이 넘어감

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

def category_page(request, slug): #프로그래밍, 문화-예술, 웹개발, no_category #context는 {중괄호 안에 넣어서 전송}
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category = None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {  #context 넘겨주기
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        },
    )

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): #createview는 폼을 만드는 놈
    model = Post
    fields = ['title', 'hook_text', 'contents', 'head_image', 'file_upload', 'category', 'tags']
    #template_name = post_form.html

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user
            #not tag
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')
