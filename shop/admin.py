from django.contrib import admin
from .models import User,Book,Order,OrderItem
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(Order)
admin.site.register(OrderItem)