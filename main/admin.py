from django.contrib import admin
from .models import Company, Type, Category, Tag, City, Country, Position




class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Type, TypeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Category, CategoryAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Tag, TagAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'country']


admin.site.register(City, CityAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Country, CountryAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'city']


admin.site.register(Company, CompanyAdmin)


class PositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


admin.site.register(Position, PositionAdmin)






