from django.contrib import admin
from .models import Courses,Category
    
admin.site.register(Courses)
# admin.site.register(Category)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['type_uz','description_uz']
    list_filter=['type_uz']
    
    search_fields=['type_uz']
