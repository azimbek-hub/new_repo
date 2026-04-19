from django.contrib import admin
from .models import Category, Product, Order, Tag, User, OrderItem, Cart


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email')
    search_fields = ('full_name', 'email')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'discount')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'customer', 'qty_items', 'amount')
    search_fields = ('order_number', 'customer__full_name')


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'order')
    search_fields = ('product__name', 'order__order_number')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order')
    search_fields = ('user__full_name',)