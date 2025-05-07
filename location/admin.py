from django.contrib import admin
from .models import Division, District, Thana

# Register your models here.
@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'bn_name', 'is_published_display', 'created_at')
    list_filter = ('is_published',)

    @admin.display(boolean=True, description='Published')
    def is_published_display(self, obj):
        return obj.is_published

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'bn_name', 'is_published_display', 'created_at')
    list_filter = ('is_published',)

    @admin.display(boolean=True, description='Published')
    def is_published_display(self, obj):
        return obj.is_published

@admin.register(Thana)
class ThanaAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'bn_name', 'is_published_display', 'created_at')
    list_filter = ('is_published',)

    @admin.display(boolean=True, description='Published')
    def is_published_display(self, obj):
        return obj.is_published