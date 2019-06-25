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
    UserAvatar = models.FileField(upload_to='media',null=True)  # 用户头像

    def __str__(self):
        return self.UserName


'''
动态表
'''


class FriendsCircleItem(models.Model):
    friendId = models.CharField(max_length=50,primary_key=True)    #id
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)  # 用户
    releaseDate = models.DateTimeField(max_length=200,null=True)  # 发布日期
    ItemText = models.TextField(max_length=500)  # 文字描述
    imgUrl = models.FileField(upload_to='media')  # 发布图片URL
    stick = models.CharField(max_length=100, null=True)  # 是否为生成的碑帖
    likeNum = models.CharField(max_length=100)  # 点赞数
    shareNum = models.CharField(max_length=100)  # 分享数

    def __str__(self):
        return self.user

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
    CollectAuthor = models.CharField(max_length=100)    #书法家
    CollectCopyName = models.CharField(max_length=100)  #碑帖名

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
    Probability = models.CharField(max_length=50)   #概率值





class HQZ(models.Model):
    Image = models.FileField(upload_to='media')    #图片





#############################################################################
#                      HealthManager
#############################################################################
'''
用户表
'''


class User(models.Model):
    account = models.CharField(max_length=100, primary_key=True)  # 账号
    password = models.CharField(max_length=100, null=False)  # 密码
    age = models.CharField(max_length=20, null=False)  # 年龄

    def __str__(self):
        return self.account


'''
疾病表
'''


class DiseasesClassify(models.Model):
    diseaseVariety = models.CharField(max_length=50, primary_key=True)  # 心脏病种类
    diseaseIntroduce = models.TextField(max_length=1000, )  # 介绍

    def __str__(self):
        return self.diseaseVariety


'''
食谱表
'''


class Foods(models.Model):
    foodId = models.IntegerField(auto_created=True, primary_key=True)  # 食物id
    foodName = models.CharField(max_length=100, null=False)  # 食物名称
    foodMaterial = models.CharField(max_length=200, )  # 食材
    foodHot = models.IntegerField()  # 热量
    foodProtein = models.IntegerField()  # 蛋白质
    foodIntroduce = models.TextField(max_length=200)  # 食物介绍
    foodUrl = models.URLField(max_length=200)  # 食物图片
    diseaseVariety = models.ForeignKey(DiseasesClassify, on_delete=models.CASCADE)  # 疾病名称，一种疾病对应多种食物

    def __str__(self):
        return self.foodName


'''
每日摄食统计表
'''



class EatStatistics(models.Model):
    eatId = models.IntegerField(auto_created=True, primary_key=True)  # 摄入食物id
    eatHot = models.IntegerField(null=False)  # 摄入热量
    eatProtein = models.IntegerField(null=False)  # 摄入蛋白质
    eatSugar = models.IntegerField(null=False)  # 摄入糖分
    eatTime = models.CharField(max_length=100)  # 摄入时间

    def __str__(self):
        return self.eatTime
