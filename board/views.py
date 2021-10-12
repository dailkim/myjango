from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q


from board.models import News

# Create your views here.
# def list(request, news_id):
#     # 글의 제목과 내용 출력
#     news = News.objects.get(id=news_id)
#     return render(request, 'news_list.html', {'news': news})

# def list(request):
#     # 글의 제목과 내용 출력
 
#     return render(request, 'news_list.html',) 

def list(request):
    # Question.objects.order_by('-create_date')
    # Question 모델에서 객체를 참조하는데 / -가 붙어 있으면 해당 객체를 기준으로 역순정렬
    # 역순으로 정렬해올것. (객체는 create_date)



    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    # 조회
    news_list = News.objects.values()
    print('log for test : ',news_list)
    # if kw:
    #     news_list = news_list.filter(
    #         Q(subject__icontains=kw) | # __icontains : 컬럼의 조회조건 부여
    #         Q(content__icontains=kw) |
    #         Q(author__username__icontains=kw) |
    #         Q(answer__author__username__icontains=kw)
    #     ).distinct()


    # 페이징처리 기능 구현
    # pagenator = Paginator(news_list, 10)# 페이지당 10개씩
    # page_obj = pagenator.get_page(page)

    context = {'news_list': news_list}

    return render(request, 'news_list.html', context)