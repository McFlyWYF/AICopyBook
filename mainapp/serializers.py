from rest_framework import serializers
from .models import CopyBookList, CopyBookAll, WordsOutline, ChinesePainting, Words, FindWords, Author,FriendsCircleItem

'''
json格式化model对象
'''


class CopyBookAllSerializer(serializers.ModelSerializer):
    CopyBookEachName = serializers.PrimaryKeyRelatedField(read_only=True, )

    class Meta:
        model = CopyBookAll
        fields = ('contentImgUrl', 'CopyBookEachName', 'CopyBookEachId',)


class CopyBookListSerializer(serializers.ModelSerializer):
    copy_book_all = CopyBookAllSerializer(source='copyBookAllSet', read_only=True, many=True)

    class Meta:
        model = CopyBookList
        fields = ('author', 'copyBookName', 'copyBookAll')


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
        fields = ('FindWordsId','FindAuthorName','FindWordName','WordsUrl')

# 书法家
class AuthorSerializer(serializers.ModelSerializer):

    AuthorWords = FindWordsSerializer(source = 'findwords_set',many=True,read_only=True)

    class Meta:
        model = Author
        fields = ('AuthorName','AuthorWords')

#朋友圈
class FriendsSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendsCircleItem
        fields = '__all__'
