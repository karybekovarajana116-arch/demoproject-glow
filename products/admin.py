from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'name',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'brand',
        'price',
        'category',
        'stock',
        'image_preview',
    )

    list_filter = (
        'category',
        'brand',
    )

    search_fields = (
        'name',
        'brand',
        'description',
    )

    def image_preview(self, obj):
        if obj.image:
            return obj.image.url

        return "Нет изображения"

    image_preview.short_description = "Изображение"
