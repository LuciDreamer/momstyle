from django.contrib import admin
from .models import (Products, Category, Keywords,
                     Carousel, Order, OrderItem,
                     AboutUsDesc, AboutUsGallery, FAQ,
                     Reviews)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'category', 'consist', 'price']
    list_filter = ['category', 'price', 'creation']



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Keywords)
class KeywordsAdmin(admin.ModelAdmin):
    pass

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    pass

class OrderItemTabular(admin.TabularInline):

     model = OrderItem
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_filter = ['closed', 'creation_date']
    inlines = [OrderItemTabular]


@admin.register(AboutUsDesc)
class AboutUsDescAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutUsGallery)
class AboutUsGalleryAdmin(admin.ModelAdmin):
    pass


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass









