#Django_prj url에서 형식 가져옴
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.PostList.as_view()),#CBV방식의 지정(views에 있는 PostList의 클래스를 보여라 라는뜻)
    #path('', views.index),#FBV방식의 지정
    #CBV방식
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page),#문자열을 slug에 담아서
    path('create_post/', views.PostCreate.as_view()), #PostCreate 클래스 참조
    path('update_post/<int:pk>/', views.PostUpdate.as_view()), #postupdate 클래스 참조
    ##댓글 부분
    path('<int:pk>/new_comment/', views.new_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('delete_comment/<int:pk>', views.delete_comment),
    #검색 부분
    path('search/<str:q>/',views.PostSearch.as_view()),
    #FBV방식
    #path('<int:pk>/', views.single_post_page),#모델을 포함시키는 형태로 만들기 위해 single_pages랑 살짝 다름
        #int:pk는 views.single_post_page 여기에 인자값으로 넘김.
]