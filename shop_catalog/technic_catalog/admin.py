from django.contrib import admin
from .models import Product, Color, Hdd


class ColorInline(admin.TabularInline):
    model = Color
    extra = 1


class HddInline(admin.TabularInline):
    model = Hdd
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_model',
                           'processor_model',
                           'processor_frequency',
                           'ram_value',
                           'display_size',
                           'videocard',
                           'video_memory_value',
                           'weight',
                           'price',
                           'image',
                           ]
                }),
        ('Options', {'fields': ['optical_drive',
                                'lte_4g',
                                'bluetooth',
                                'wi_fi',],
                     'classes': ['collapse']}),

    ]
    inlines = [ColorInline, HddInline]
    search_fields = ['product_model']


admin.site.register(Product, ProductAdmin)
#admin.site.register(Color)
#admin.site.register(Hdd)
