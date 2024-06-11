from django.shortcuts import render, redirect
from .models import Post,Category,Tag, Comment #모델을 가져오고 그 안에 있는 Post클래스 가져오기
from django.views.generic import ListView, DetailView,CreateView, UpdateView # 장고가 가지고 있는 클래스들 리스트를 볼수 있고 하나하나 볼수있는 페이지
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .forms import CommentForm
from django.shortcuts import get_object_or_404 #db에서 하나만 가져오는 명령어
from django.db.models import Q
# Create your views here.

#CBV 방식
class PostList(ListView):
    model = Post #자동적으로 post_list로 저장 따라서 view파일에 posts를 쓴것을 바꿔줘야함
    #template_name = 'blog/index.html' #템플릿 지정 (지정안하면 post_list로 자동지정)
    ordering = '-pk' #오름차순, 내림차순 지정

    paginate_by = 2 ##한페이지에 몇개씩 보여줄 건지

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
        context['comment_form'] = CommentForm #form.py에서 만든걸 comment_form변수에 넣음
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

#/blog/create_post/
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView): #createview는 폼을 만드는 놈
    model = Post
    fields = ['title', 'hook_text', 'contents', 'head_image', 'file_upload', 'category', 'tags'] #이미 로그인이 되어있어 user가 빠짐
    #template_name = post_form.html 자동으로 열림

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff #관리자 계정이거나 staff계정이거나 확인

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):#로그인만 되면 되겠금 할려면 뒷부분날리기
            form.instance.author = current_user
            #not tag
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

#/blog/update_post/pk
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'contents', 'head_image', 'file_upload', 'category', 'tags'] #이미 로그인이 되어있어 user가 빠짐
    #기본 템플릿 post_form.html 따라서 생성할때랑 공유하게 됨 따라서 다른 템플릿 사용
    template_name = "blog/post_update_form.html"
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
def csrf_failure(request, reason=""):
    return redirect('/blog/')

def new_comment(request, pk):  #댓글 쓰기 함수
    if request.user.is_authenticated:
        post = get_object_or_404(Post, pk=pk)

        if request.method == "POST":
            comment_form = CommentForm(request.POST) #폼 가져오기
            if comment_form.is_valid(): #폼이 정상적이라면
                comment = comment_form.save(commit=False)#commit은 임시저장의 기능
                comment.post = post
                comment.author = request.user #필요한 부분 채우기 날짜, 시간 등등
                comment.save()
                return redirect(comment.get_absolute_url())
        else:
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

def delete_comment(request, pk): #댓글 지우기 함수
    comment = get_object_or_404(Comment, pk= pk)
    post = comment.post
    if request.user.is_authenticated and request.user == comment.author:
        comment.delete()
        return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied

class CommentUpdate(LoginRequiredMixin,UpdateView): #댓글 수정하기 클래스
    model = Comment
    form_class = CommentForm #별도로 폼을 만들어놔서 자동생성을 안쓰고 만듣어 놓은거 사용
    #comment_form.html을 찾으려고 함
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(CommentUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

#검색 기능 클래스 class PostList(ListView)를 상속 => post_list.html
    #def get_queryset(self):
            #post_list = Post.objects.all  이라는 것이 생략 되어있음 따라서 오버라이딩을 해서 다른걸 동작하게 만듬
class PostSearch(PostList):
    paginate_by = None

    def get_queryset(self):
        q = self.kwargs['q'] #q = 서치할 단어
        post_list = Post.objects.filter(
            Q(title__contains=q) | Q(tags__name__contains=q)
        ).distinct() #distinct는 중복을 하나로 만드는 것
        return post_list

    def get_context_data(self, **kwargs):
        context = super(PostSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'

        return context