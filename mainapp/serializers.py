from rest_framework import serializers
from .models import CopyBookList, CopyBookAll, WordsOutline, ChinesePainting, Words, FindWords, Author, \
    FriendsCircleItem, MyUser, Collectors

'''
json格式化model对象
'''


class CopyBookAllSerializer(serializers.ModelSerializer):
    CopyBookEachName = serializers.PrimaryKeyRelatedField(read_only=True, )

    class Meta:
        model = CopyBookAll
        fields = ('contentImgUrl', 'CopyBookEachName', 'CopyBookEachId',)


class CopyBookListSerializer(serializers.ModelSerializer):
    copy_book_all = CopyBookAllSerializer(source='copybookall_set', read_only=True, many=True)

    class Meta:
        model = CopyBookList
        fields = ('author', 'copyBookName', 'copy_book_all')


# 朋友圈
class FriendsSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True, )

    class Meta:
        model = FriendsCircleItem
        fields = ('user', 'releaseDate', 'ItemText', 'imgUrl', 'stick', 'likeNum', 'shareNum')


# 用户
class MyUserSerializer(serializers.ModelSerializer):
    friends_circle_item = FriendsSerializer(source='friendscircleitem_set', read_only=True, many=True)

    class Meta:
        model = MyUser
        fields = ('UserName', 'UserAge', 'UserAvatar', 'friends_circle_item')


# 收藏
class CollectSerializer(serializers.ModelSerializer):
    # CollectUser = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = Collectors
        fields = ('CollectId', 'CollectUser', 'CollectUrl', 'CollectAuthor', 'CollectCopyName')


#
# #用户收藏
# class MyUserSerializerT(serializers.ModelSerializer):
#
#     collection = CollectSerializer(source='collect_set',read_only=True,many=True)
#
#     class Meta:
#         model = MyUser
#         fields = ('UserName','UserAge','UserAvatar','collection')


# 轮廓
class WordsOutlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordsOutline
        fields = '__all__'


# 国画
class ChinesePaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChinesePainting
        fields = '__all__'


# 字
class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'


# 查找
class FindWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FindWords
        fields = ('FindWordsId', 'FindAuthorName', 'FindWordName', 'WordsUrl', 'Probability')


# 书法家
class AuthorSerializer(serializers.ModelSerializer):
    AuthorWords = FindWordsSerializer(source='findwords_set', many=True, read_only=True)

    class Meta:
        model = Author
        fields = ('AuthorName', 'AuthorWords')
