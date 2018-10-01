from django.db import models

# Create your models here.

'''
首页所有书法家碑帖表
'''


class CopyBookList(models.Model):
    copyBookName = models.TextField(max_length=100, primary_key=True)  # 碑帖名
    author = models.CharField(max_length=30)  # 书法家名

    def __str__(self):
        return self.copyBookName


'''
所有碑帖图片表
'''


class CopyBookAll(models.Model):
    CopyBookEachId = models.CharField(max_length=100, primary_key=True)  # 碑帖ID
    CopyBookEachName = models.ForeignKey(CopyBookList, on_delete=models.CASCADE)  # 碑帖名字
    contentImgUrl = models.URLField(max_length=200)  # 详情URL

    def __str__(self):
        return self.CopyBookEachName


'''
用户表
'''


class MyUser(models.Model):
    UserName = models.CharField(max_length=100, primary_key=True)  # 用户名
    UserPassword = models.CharField(max_length=100)  # 密码
    UserAge = models.CharField(max_length=50, null=True)  # 年龄段
    UserAvatar = models.FileField(upload_to='media')  # 用户头像

    def __str__(self):
        return self.UserName


'''
动态表
'''


class FriendsCircleItem(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)  # 用户
    releaseDate = models.DateTimeField(max_length=200)  # 发布日期
    ItemText = models.TextField(max_length=500)  # 文字描述
    imgUrl = models.URLField(max_length=100)  # 发布图片URL
    stick = models.CharField(max_length=100, null=True)  # 是否为生成的碑帖
    likeNum = models.CharField(max_length=100)  # 点赞数
    shareNum = models.CharField(max_length=100)  # 分享数


'''
字体轮廓表
'''


class WordsOutline(models.Model):
    WordName = models.CharField(max_length=50, primary_key=True)  # 字体轮廓名
    WordAuthor = models.CharField(max_length=50)  # 书法家名
    WordUrl = models.URLField(max_length=200)  # 轮廓URL

    def __str__(self):
        return self.WordName


'''
国画表
'''


class ChinesePainting(models.Model):
    PaintingId = models.CharField(max_length=50, primary_key=True)  # 国画ID
    PaintingUrl = models.URLField(max_length=200)  # 国画URL

    def __str__(self):
        return self.PaintingId


'''
收藏品表
'''


class Collectors(models.Model):
    CollectId = models.CharField(max_length=50, primary_key=True)  # 收藏品ID
    CollectUrl = models.URLField(max_length=100)  # 收藏品URL
    CollectUser = models.ForeignKey(MyUser, on_delete=models.CASCADE)  # 用户

    def __str__(self):
        return self.CollectId


'''
单字列表
'''


class Words(models.Model):
    WordName = models.CharField(max_length=50, primary_key=True)  # 字名

    def __str__(self):
        return self.WordName


'''
书法家表
'''


class Author(models.Model):
    AuthorName = models.CharField(max_length=50, primary_key=True)  # 书法家名
    AuthorWords = models.ManyToManyField(Words, through='FindWords')

    def __str__(self):
        return self.AuthorName


'''
根据书法家查找相应的字
'''


class FindWords(models.Model):
    FindWordsId = models.CharField(max_length=50, primary_key=True)  # ID
    FindAuthorName = models.ForeignKey(Author, on_delete=models.CASCADE)  # 书法家名
    FindWordName = models.ForeignKey(Words, max_length=50, on_delete=models.CASCADE)  # 字名
    WordsUrl = models.URLField(max_length=200)  # URL
