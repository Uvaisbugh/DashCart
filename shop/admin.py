from django.contrib import admin

# Register your models here.
from . models import category,Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated','image']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)


