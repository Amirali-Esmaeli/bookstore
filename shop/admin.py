from django.contrib import admin
from .models import User,Book,Order,OrderItem,Category
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}