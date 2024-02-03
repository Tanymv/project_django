from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category",)
    list_filter = ("category",)
    search_fields = ("title", "description",)

    def description(self, obj):
        return obj.body[:100]


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number', 'is_active')
    list_filter = ('is_active',)
