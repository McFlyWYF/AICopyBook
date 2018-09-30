from django.conf.urls import url, include
from rest_framework import routers
from mainapp import views

app_name = '[mainapp]'

router = routers.DefaultRouter()
router.register(r'copybookList', views.copyBookListSet)  # 碑帖列表
router.register(r'copybookAll', views.copyBookAllSet)  # 所有碑帖图片
router.register(r'WordsOutline', views.WordsOutlineSet)  # 字轮廓
router.register(r'ChinesePainting', views.ChinesePaintingSet)  # 国画
router.register(r'findwords', views.FindWordsSet)  #提取字


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
