from django.contrib import admin
from .models import (
    Profile, Author, Category, Book,
    Favorite, ReadingHistory, Review,
    Payment, BookView
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'pages')
    search_fields = ('title', 'isbn')
    list_filter = ('author', 'category')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'book')
    search_fields = ('user__username', 'book__title')


@admin.register(ReadingHistory)
class ReadingHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'read_at')
    search_fields = ('user__username', 'book__title')
    list_filter = ('read_at',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'rating', 'created_at')
    search_fields = ('user__username', 'book__title')
    list_filter = ('rating', 'created_at')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'amount', 'paid_at')
    search_fields = ('user__username', 'book__title')
    list_filter = ('paid_at',)


@admin.register(BookView)
class BookViewAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'viewed_at')
    search_fields = ('user__username', 'book__title')
    list_filter = ('viewed_at',)