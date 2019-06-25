from django.contrib import admin

# Register your models here.

from .models import Foods,DiseasesClassify,EatStatistics,User


class FoodsAdmin(admin.ModelAdmin):
    fields = ['foodId','foodName','foodMaterial','foodHot','foodProtein','foodIntroduce','foodUrl','diseaseVariety']

admin.site.register(Foods,FoodsAdmin)

# class FoodsInline(admin.StackedInline):


class DiseaseAdmin(admin.ModelAdmin):
    fields = ['diseaseVariety','diseaseIntroduce']
    # inlines = [FoodsAdmin]

admin.site.register(DiseasesClassify,DiseaseAdmin)

class EatAdmin(admin.ModelAdmin):
    fields = ['eatId','eatHot','eatProtein','eatSugar','eatTime']

admin.site.register(EatStatistics,EatAdmin)

class UserAdmin(admin.ModelAdmin):
    fields = ['account','password','age']

admin.site.register(User,UserAdmin)