from django.conf.urls import url, include
from rest_framework import routers
from mainapp import views

app_name = '[mainapp]'

router = routers.DefaultRouter()
router.register(r'copybookList', views.copyBookListSet)  # 碑帖列表
router.register(r'copybookAll', views.copyBookAllSet)  # 所有碑帖图片-
router.register(r'WordsOutline', views.WordsOutlineSet)  # 字轮廓
router.register(r'ChinesePainting', views.ChinesePaintingSet)  # 国画
router.register(r'findwords', views.FindWordsSet)  # 提取单个字
router.register(r'friendsAll', views.FriendsCircleItemSet)  # 朋友圈所有动态-
router.register(r'showFriends', views.MyUserSet)  # 所有用户的动态
router.register(r'showCollections', views.CollectSet)  # 收藏

###################################################################

router.register(r'user', views.UserSet)  # 用户
router.register(r'foods', views.FoodsSet)  # 食谱
router.register(r'disease', views.DiseasesClassifySet)  # 疾病分类
router.register(r'eat', views.EatStatisticsSet)  # 摄入统计

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
