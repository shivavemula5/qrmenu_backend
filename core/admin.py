from django.contrib import admin

from core.models import Place , Category , MenuItem

class CategoryInline(admin.StackedInline):
    model = Category

class MenuItemInline(admin.StackedInline):
    model = MenuItem

class PlaceAdmin(admin.ModelAdmin):
    inlines = [CategoryInline,MenuItemInline]

class CategoryAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]

class MenuItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Place,PlaceAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(MenuItem,MenuItemAdmin)
