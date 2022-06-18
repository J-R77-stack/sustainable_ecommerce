from django.contrib import admin
from .models import Product, Category, ProductReviews


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'stars',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )

class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'content',
        'stars',
        'date_added',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReviews, ProductReviewsAdmin)
