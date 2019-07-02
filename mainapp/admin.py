from django.contrib import admin

# Register your models here.

from .models import Foods, DiseasesClassify, EatStatistics, User

admin.site.site_header = '基于心脏病的健康管理'
admin.site.site_title = '基于心脏病的健康管理'


class FoodsAdmin(admin.ModelAdmin):
    fields = ['foodId', 'foodName', 'foodMaterial', 'foodHot', 'foodProtein', 'foodIntroduce', 'foodUrl',
              'diseaseVariety']

    list_display = ('foodId', 'foodName', 'foodHot', 'foodProtein', 'foodIntroduce')


admin.site.register(Foods, FoodsAdmin)


class DiseaseAdmin(admin.ModelAdmin):
    fields = ['diseaseVariety', 'diseaseIntroduce']

    list_display = ('diseaseVariety', 'diseaseIntroduce')


admin.site.register(DiseasesClassify, DiseaseAdmin)


class EatAdmin(admin.ModelAdmin):
    fields = ['eatId', 'eatHot', 'eatProtein', 'eatSugar', 'eatTime']

    list_display = ('eatId', 'eatHot', 'eatProtein', 'eatSugar', 'eatTime')


admin.site.register(EatStatistics, EatAdmin)


class UserAdmin(admin.ModelAdmin):
    fields = ['account', 'password', 'age']

    list_display = ('account', 'password', 'age')

admin.site.register(User, UserAdmin)

