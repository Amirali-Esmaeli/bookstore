from django.db import models
from django.contrib.auth.models import AbstractUser,Permission,Group
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator
# Create your models here.

class User(AbstractUser):
    address = models.TextField(_("آدرس"), blank = True, null = True)
    phone_number = models.CharField(
        _("شماره تلفن"), 
        max_length = 11, 
        blank = True, 
        null = True,
        validators = [RegexValidator(regex=r'^\d{11}$', message="شماره تلفن باید 11 رقم باشد.")])
    groups = models.ManyToManyField(Group, related_name="shop_users")
    user_permissions = models.ManyToManyField(Permission, related_name="shop_user_permissions")

    def __str__(self):
        return self.username 

class Book(models.Model):
    title = models.CharField(_("عنوان"), max_length=255)
    author = models.CharField(_("نویسنده"), max_length=255)   
    description = models.TextField(_("توضیحات"))
    price = models.IntegerField(_("قیمت"))
    image = models.ImageField(upload_to='books/', blank=True , null=True)
    stock = models.IntegerField(_("موجودی") , default=10)

    def __str__(self):
        return self.title

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE ,related_name="orders")
    books = models.ManyToManyField(Book,through='OrderItem', related_name="orders")
    status = models.CharField(
        _("وضعیت"), 
        max_length=20,
        choices=[('pending', 'در انتظار'), ('completed', 'تکمیل شده')],
        default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.quantity * item.book.price for item in self.order_items.all())

    def __str__(self):
        return f"سفارش {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="order_items")
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="order_items")
    quantity = models.PositiveIntegerField(_("تعداد"),default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.title}"