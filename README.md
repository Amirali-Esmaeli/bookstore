<div dir="rtl">

# فروشگاه آنلاین کتاب
یه پروژه فروشگاهی ساده و کاربردی که با **Django** ساخته شده و قابلیت‌های اصلی یه فروشگاه آنلاین رو داره. این پروژه برای یادگیری مفاهیم بک‌اند و آماده‌سازی برای کارآموزی طراحی شده.

## ویژگی‌ها
- **مدیریت محصولات:** نمایش لیست کتاب‌ها، جزئیات هر کتاب (عنوان، نویسنده، قیمت، موجودی)
- **سبد خرید:** اضافه کردن، به‌روزرسانی تعداد و حذف کتاب‌ها از سبد خرید با استفاده از سشن
- **سفارش‌ها:** ثبت سفارش و نمایش تاریخچه سفارش‌ها برای هر کاربر
- **احراز هویت:** ثبت‌نام، ورود، خروج، تغییر رمز عبور و بازنشانی رمز عبور
- **جستجو:** فیلتر کردن کتاب‌ها بر اساس عنوان یا نویسنده
- **رابط کاربری:** طراحی responsive با **Bootstrap 5**
- **تست:** تست‌های واحد (Unit Tests) برای اطمینان از عملکرد صحیح ویوها و مدل‌ها

## تکنولوژی‌ها
- **Django 4.x**: فریم‌ورک اصلی بک‌اند
- **MySQL**: دیتابیس استفاده شده در این پروژه
- **Bootstrap 5**: برای رابط کاربری
- **Python 3.x**: زبان برنامه‌نویسی

## نصب و راه‌اندازی
1. **پیش‌نیازها:**
   - Python 3.8 یا بالاتر
   - Git
   - MySQL (برای استفاده از دیتابیس MySQL در پروژه)
   - Pillow (برای پردازش تصاویر)

2. **کلون کردن پروژه:**
   ```bash
   git clone https://github.com/Amirali-Esmaeli/bookstore.git
   cd bookstore

3. **ایجاد محیط مجازی (اختیاری اما توصیه شده):**
    ```bash
    python -m venv venv
    ```
    در Windows:
    ```cmd
    venv\Scripts\activate
    ```
    در Linux/Mac:
    ```bash
    source venv/bin/activate
    ```

4. **نصب وابستگی‌ها:**
    ```bash
    pip install -r requirements.txt
    ```

5. **پیکربندی دیتابیس:**
    ```cmd
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore_db',  # نام دیتابیست رو بسازید
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
        }
    }

6. **اجرای مهاجرت‌ها:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

7. **ایجاد کاربر ادمین:**
    ```bash
    python manage.py createsuperuser

8. **اجرای پروژه:**
    ```bash
    python manage.py runserver
    ```
    برو http://127.0.0.1:8000/ حالا به آدرس 

9. **اجرای تست ها:**
    ```bash
    python manage.py test

**ساختار پروژه:**

- `shop/models.py` : تعریف مدل‌های `User`، `Book`، `Order` و `OrderItem`
- `shop/admin.py` : ثبت مدل‌ها در پنل ادمین Django
- `shop/views.py` : منطق مربوط به ویوهای بک‌اند
- `shop/urls.py` : تعریف مسیرهای URL اپلیکیشن
- `shop/forms.py` : فرم‌های سفارشی برای ورود، ثبت‌نام، تغییر رمز عبور و غیره
- `shop/templates/shop/` : قالب‌های HTML مربوط به صفحات مختلف
- `shop/tests.py` : شامل تست‌های واحد (unit tests) برای بررسی عملکرد بخش‌های مختلف

**نکات اضافی**

- برای اضافه کردن کتاب، از پنل ادمین (/admin/) استفاده کن
- بازنشانی رمز عبور توی کنسول چاپ می‌شه (برای تست محلی)

**توسعه‌دهنده**

- **نام:** امیرعلی اسماعیلی  
- **ایمیل:** [amiraliesmaeli741@gmail.com](mailto:amiraliesmaeli741@gmail.com)  
- **گیت‌هاب:** [github.com/Amirali-Esmaeli](https://github.com/Amirali-Esmaeli?tab=repositories)
</div> 

# Online Bookstore
A simple and functional online bookstore project built with Django, featuring core e-commerce functionalities. This project was designed to learn backend concepts and prepare for a backend internship.

## Features

- **Product Management**: Display book list and details (title, author, price, stock)  
- **Shopping Cart**: Add, update quantity, and remove books from the cart using sessions  
- **Orders**: Place orders and view order history per user  
- **Authentication**: Sign up, login, logout, password change, and password reset  
- **Search**: Filter books by title or author  
- **User Interface**: Responsive design with Bootstrap 5  
- **Testing**: Unit tests to ensure proper functionality of views and models  

## Technologies
**Django 4.x**: Main backend framework
**MySQL**: Database used in this project
**Bootstrap 5**: For the user interface
**Python 3.x**: Programming language

## Installation and Setup
1. **Prerequisites:**
- Python 3.8 or higher
- Git
- MySQL (for using MySQL database)
- Pillow (for image processing)

2. **Clone the Project:**
    ```bash
    git clone https://github.com/Amirali-Esmaeli/bookstore.git
    cd bookstore

3. **Create a Virtual Environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```
    On Windows:
    ```cmd
    venv\Scripts\activate
    ```
    On Linux/Mac:
    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Database Configuration: In settings.py:**
   ```cmd
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore_db',  # Create your database
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
        }
    }

6. **Run Migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate

7. **Create Admin User:**
    ```bash
    python manage.py createsuperuser

8. **Run the Project:**
    ```bash
    python manage.py runserver
    ```
    Go to http://127.0.0.1:8000/.

9. **Run Tests:**
    ```bash
    python manage.py test shop

**Project Structure**
- `shop/models.py`: Defines `User`, `Book`, `Order`, `OrderItem` models
- `shop/admin.py`: Registers models in Django admin panel
- `shop/views.py`: Backend logic for views
- `shop/urls.py`: URL routes
- `shop/forms.py`: Custom forms for login, signup, and password change
- `shop/templates/shop/`: HTML templates
- `shop/tests.py`: Unit tests

**Additional Notes**
- Add books via the admin panel (/admin/).
- Password reset links are printed to the console (for local testing).

**Developer**

- **Name**: Amirali Esmaeli
- **Email**: [amiraliesmaeli741@gmail.com](mailto:amiraliesmaeli741@gmail.com)
- **GitHub**: [https://github.com/Amirali-Esmaeli](https://github.com/Amirali-Esmaeli?tab=repositories)

