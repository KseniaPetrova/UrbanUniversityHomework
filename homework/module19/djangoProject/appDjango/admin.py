from django.contrib import admin
from .models import Category, News
# Register your models here.

#АДМИНКА ДЛЯ МОДЕЛИ Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Поля для отображения в списке
    search_fields = ('name',)  # Поля для поиска

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'create_at', 'is_published')  # Поля для отображения
    list_filter = ('category', 'is_published')  # Фильтрация по категории и статусу публикации
    search_fields = ('title', 'content')  # Поля для поиска
    list_per_page = 10  # Количество новостей на странице

    # Разбиение полей на секции
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'category')
        }),
        ('Дополнительные настройки', {
            'classes': ('collapse',),  # скрыть секцию по умолчанию
            'fields': ('is_published', 'create_at', 'update_at')
        }),
    )

    # Только для чтения полей created_at и updated_at
    readonly_fields = ('create_at', 'update_at')












