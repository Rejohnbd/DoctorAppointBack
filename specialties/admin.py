from django.contrib import admin
from .models import Specialty

# Register your models here.
@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_published_display', 'created_at')
    list_filter = ('is_published',)

    @admin.display(boolean=True, description='Published')
    def is_published_display(self, obj):
        return obj.is_published
