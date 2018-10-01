from rest_framework import viewsets, status
from mainapp.serializers import CopyBookListSerializer, CopyBookAllSerializer, \
    ChinesePaintingSerializer, WordsOutlineSerializer, WordsSerializer, FindWordsSerializer, AuthorSerializer
from .models import CopyBookList, CopyBookAll, ChinesePainting, WordsOutline, Words, FindWords, Author, MyUser, \
    Collectors, FriendsCircleItem
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


# 注册
@csrf_exempt
def register(request):
    if request.method == 'POST':

        account = request.POST.get('account')  # 用户名
        password = request.POST.get('password')  # 密码
        age = request.POST.get('age')  # 年龄段
        avatar = request.FILES.get('avatar')  # 头像，通过127.0.0.1:8000/media/图片名访问头像

        user = models.MyUser.objects.create(UserName=account, UserPassword=password, UserAge=age, UserAvatar=avatar)
        user.save()
        print(avatar)

        return HttpResponse('注册成功')
    else:
        return HttpResponse('用户已存在')


# 登录
@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('account')  # 用户名
        password = request.POST.get('password')  # 密码
        # print(username,password)
        users = MyUser.objects.filter(UserName=username, UserPassword=password)
        # print(users)
        if users:
            return HttpResponse('登录成功')

        else:
            return HttpResponse('登录失败')


# 收藏
@csrf_exempt
def collection(request):
    if request.method == 'POST':
        id = request.POST.get('id')  # 收藏品编号
        url = request.POST.get('url')  # 收藏品URL
        user = request.POST.get('user')  # 用户名

        users = Collectors.objects.create(CollectId=id, CollectUrl=url, CollectUser_id=user)
        users.save()
        return HttpResponse('收藏成功')


# 朋友圈
@csrf_exempt
def friend(request):
    if request.method == 'POST':
        id = request.POST.get('id')  # 动态编号
        date = request.POST.get('date')  # 发布日期
        text = request.POST.get('text')  # 文本内容
        url = request.POST.get('url')  # 图片URL
        stick = request.POST.get('stick')  # 是否是生成的碑帖
        likenum = request.POST.get('likenum')  # 点赞数
        sharenum = request.POST.get('sharenum')  # 分享数
        user = request.POST.get('user')  # 用户名

        users = FriendsCircleItem.objects.create(id=id, releaseDate=date, ItemText=text, imgUrl=url, stick=stick,
                                                 likeNum=likenum, shareNum=sharenum, user_id=user)
        users.save()
        return HttpResponse('发布成功')
