from django.http import HttpResponse
from django.shortcuts import  render
from django.urls import reverse
from app1.models import Person,Article,Tag
from django.db.models import Count
from .forms import AddForm
import os

def index(request):
    return HttpResponse( u'hello 你好，jee')
# Create your views here.

def getfun(request,a,b):
    # a = request.GET.get('a', '0') # 0是默认值
    # b = request.GET.get('b', '0') # b = request.GET['b'] 这样写没有传递b时会报错

    # return HttpResponse( str(int(a)+int(b))+a)
    # sum=int(a)+int(b)
    zidian = {'firstName':'蘇','name':'應亮'}
    Person.objects.get_or_create(name=u"李三", age="33") #插入数据库
    get1=Person.objects.get(name=u'苏应亮') # 查询数据库 get一个对象
    get1.age='999'
    get1.save()
    Person.objects.all()[0:]
    Person.objects.filter(name__contains='苏').exclude(age=32)
    sjk = Article.objects.values_list('id','title','score') #元组形式
    sjk1 = Article.objects.values('id', 'title', 'score','author','author__name','author__age')  # 字典形式 author__name是外键表里的内容
    sjk2 = Article.objects.filter(author__name='苏应亮').values_list('title', flat=True)  # 单个字段

    num = Person.objects.values('name').annotate(count=Count('author_name')).values('name','count')#作者和作者的文章数

    sql = Person.objects.values('name').annotate(count=Count('age')).values('name','count').query

    if request.method == 'POST':

        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            cnum = int(a)+int(b)
    else:
        form = AddForm()
        cnum = '0'


    BASE_DIR = os.path.dirname(__file__)
    return render(request, 'getfun.html',{
        'sum':int(a)+int(b),
        'zidian':zidian,
        'liebiao':range(1,100),
        'sjk':sjk,
        'sjk1':sjk1,
        'sjk2':sjk2,
        'num':num,
        'sql':sql,
        'form':form,
        'cnum':cnum,
        'BASE_DIR':BASE_DIR

    })

def add(request,a,b):
    url = reverse('getfun', args=(1,25))
    return HttpResponse( str(int(a)+int(b))+url)

def create_article(request):
    articles = ['Django 教程', 'Python 教程', 'HTML 教程']

    for i in articles:
        content = i+'dsfdsfdsafdsafdafdsa'
        import random
        author = random.randrange(1,5)
        Article.objects.get_or_create(title=i, score=100, content=content,author_id=author)  # 插入数据库
    return HttpResponse('success')
