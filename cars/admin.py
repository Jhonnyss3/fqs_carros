from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'brand', 'model', 'year',
        'price', 'fuel', 'status', 'is_featured', 'created_at',
    )
    list_filter = (
        'status', 'fuel', 'transmission', 'body_type',
        'is_featured', 'is_negotiable', 'brand',
    )
    search_fields = ('title', 'brand', 'model', 'plate', 'description')
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
