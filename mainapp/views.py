from rest_framework import viewsets, status
from mainapp.serializers import CopyBookListSerializer, CopyBookAllSerializer, \
    ChinesePaintingSerializer, WordsOutlineSerializer, WordsSerializer, FindWordsSerializer, AuthorSerializer
from .models import CopyBookList, CopyBookAll, ChinesePainting, WordsOutline, Words, FindWords, Author
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import HttpResponse
import json


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


from django.contrib import auth
from .models import MyUser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect


@csrf_exempt
def register(request):
    account = None
    password = None
    password2 = None
    age = None
    CompareFlag = False

    if request.method == 'POST':
        if not request.POST.get('account'):
            print('用户名不能为空')

        else:
            account = request.POST.get('account')

        if not request.POST.get('password'):
            print('密码不能为空')

        else:
            password = request.POST.get('password')

        if not request.POST.get('password2'):
            print('确认密码不能为空')

        else:
            password2 = request.POST.get('password2')

        if not request.POST.get('age'):
            print('年龄不能为空')

        else:
            age = request.POST.get('age')

        if password is not None:
            if password == password2:
                CompareFlag = True

            else:
                print('两次密码不一致')

        if account is not None and password is not None and password2 is not None and age is not None and CompareFlag:
            user = MyUser.objects.create(account,password,age)
            user.save()

    return render(request,'user')


