from django.contrib import admin
from .models import Car, Brand, CarImage


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 3


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = (
        'id', 'title', 'brand', 'model', 'year',
        'price', 'fuel', 'status', 'is_featured', 'created_at',
    )
    list_filter = (
        'status', 'fuel', 'transmission', 'body_type',
        'is_featured', 'is_negotiable', 'brand',
    )
    search_fields = ('title', 'brand__name', 'model', 'plate', 'description')
    list_editable = ('status', 'is_featured')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    fieldsets = (
        ('Anúncio', {
            'fields': ('title', 'subtitle', 'description'),
        }),
        ('Identificação', {
            'fields': ('brand', 'model', 'version', 'year', 'color', 'plate'),
        }),
        ('Especificações Técnicas', {
            'fields': (
                'fuel', 'transmission', 'body_type',
                'engine', 'horsepower', 'mileage', 'doors',
            ),
        }),
        ('Preço', {
            'fields': ('price', 'is_negotiable'),
        }),
        ('Status', {
            'fields': ('status', 'is_featured'),
        }),
        ('Mídia', {
            'fields': ('thumbnail',),
        }),
        ('Log', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
