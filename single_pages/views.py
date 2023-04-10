from django.shortcuts import render

# Create your views here.

def landing(request): #request는 유저의 요청을 의미
    return render(#render는 사용자에게 보내주는 것
        request,
        'single_pages/landing.html', #single_pages에다가 바로 html을 만들면 안됨!!
        # #템플릿 폴더 안에서 찾으라는 의미이기 때문에 템플릿 폴더 생성하고 single_pages하위폴더 생성하기!!
        #템플릿 폴더는 반드시 templates
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
    )