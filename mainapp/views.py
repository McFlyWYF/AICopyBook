from rest_framework import viewsets, status
from mainapp.serializers import CopyBookListSerializer, CopyBookAllSerializer, \
    ChinesePaintingSerializer, WordsOutlineSerializer, WordsSerializer, FindWordsSerializer, AuthorSerializer
from .models import CopyBookList, CopyBookAll, ChinesePainting, WordsOutline, Words, FindWords, Author
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import HttpResponse
from mainapp import models


# Create your views here.


class copyBookListSet(viewsets.ModelViewSet):
    '''
    查询数据库中的所有碑帖
    :param request:
    :return:
    '''

    queryset = CopyBookList.objects.all()
    serializer_class = CopyBookListSerializer
    lookup_field = 'copyBookName'


class copyBookAllSet(viewsets.ModelViewSet):
    '''
    查询数据库中的对应碑帖的所有图片
    '''
    queryset = CopyBookAll.objects.all()
    serializer_class = CopyBookAllSerializer
    lookup_field = 'CopyBookEachName'


class ChinesePaintingSet(viewsets.ModelViewSet):
    '''
    国画
    '''

    queryset = ChinesePainting.objects.all()
    serializer_class = ChinesePaintingSerializer


class WordsOutlineSet(viewsets.ModelViewSet):
    '''
    轮廓
    '''

    queryset = WordsOutline.objects.all()
    serializer_class = WordsOutlineSerializer


class WordsSet(viewsets.ModelViewSet):
    '''
    单个字
    '''

    queryset = Words.objects.all()
    serializer_class = WordsSerializer


class AuthorSet(viewsets.ModelViewSet):
    '''
    书法家
    '''

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class FindWordsSet(viewsets.ModelViewSet):
    '''
    查找
    '''

    queryset = FindWords.objects.all()
    serializer_class = FindWordsSerializer

    def list(self, request, *args, **kwargs):
        auths = self.queryset.filter(FindAuthorName=request.GET['author'], FindWordName=request.GET['word'])
        serializer = FindWordsSerializer(auths, many=True)
        return Response(serializer.data)


from django.views.decorators.csrf import csrf_exempt
from .forms import RegisterForm

'''
#注册
@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        

        account = request.POST.get('account')

        password = request.POST.get('password')

        # password2 = request.POST['password2']

        age = request.POST.get('age')

        user = models.MyUser.objects.create(UserName=account, UserPassword=password, UserAge=age)
        print(type(user), user)
        user.save()

    return HttpResponse('注册成功')
'''

from .models import MyUser
from .forms import RegisterForm, LoginForm


@csrf_exempt
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            age = form.cleaned_data['age']
            user = MyUser.objects.create(UserName=username, UserPassword=password1, UserAge=age)
            user.save()
            return HttpResponse('注册成功')



@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            namefilter = MyUser.objects.filter(UserName=username, UserPassword=password)
            if len(namefilter) > 0:
                return HttpResponse('登录成功')

            else:
                return HttpResponse('请重新输入密码')
