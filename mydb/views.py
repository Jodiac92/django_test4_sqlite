from django.shortcuts import render
from mydb.models import Article

# Create your views here.
def Main(request):
    return render(request, 'main.html') #main.html뿌려줘~

def ListFunc(request):
    datas = Article.objects.all() #ORM : select * from article <-이 일이 실행된거야, 그 결과를 datas에 객체로 담김
    #print(datas[0].name) #손정훈
    return render(request, 'show.html', {'datas': datas})#show.html로 datas라는 키에다가 datas를 담아서 갈거야(dict타입)
    