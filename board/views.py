from django.shortcuts import render

from board.models import News

# Create your views here.
# def list(request, news_id):
#     # 글의 제목과 내용 출력
#     news = News.objects.get(id=news_id)
#     return render(request, 'news_list.html', {'news': news})

def list(request):
    # 글의 제목과 내용 출력
 
    return render(request, 'news_list.html',) 