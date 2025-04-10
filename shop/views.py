from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Order, OrderItem,Category
from .forms import (CustomUserCreationForm,CustomAuthenticationForm,CustomPasswordChangeForm,
                    CustomPasswordResetForm,CustomPasswordResetConfirmForm)
from django.contrib.auth.views import (PasswordChangeView,PasswordResetView,PasswordResetDoneView,
                                       PasswordResetConfirmView,PasswordResetCompleteView)
from django.urls import reverse_lazy

# Create your views here.

def book_list(request):
    category_id = request.GET.get('category')
    categories = Category.objects.all()
    if category_id:
        books = Book.objects.filter(categories__id=category_id)
    else:
        books = Book.objects.all()
    return render(request, 'shop/book_list.html', {'books':books ,'categories': categories,
        'selected_category': category_id})

def category_detail(request,slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(categories=category)
    return render(request, 'shop/category_detail.html', {
        'category': category,
        'books': books
    })

def book_detail(request,book_id):
    book = get_object_or_404(Book , id=book_id)
    return render(request, 'shop/book_detail.html', {'book':book} )

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'shop/signup.html', {'form': form})

def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request.POST, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('book_list')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'shop/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('book_list')

def add_to_cart(request,book_id):
    book = get_object_or_404(Book, id=book_id)
    cart = request.session.get('cart',{})
    book_id = str(book_id)
    cart[book_id] = cart.get(book_id,0) + 1
    request.session['cart'] = cart
    return redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart',{})
    cart_items = []
    total_price = 0
    price = 0
    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, id=book_id)
        price += book.price * quantity
        total_price += book.price * quantity
        cart_items.append({'book':book,'quantity':quantity ,'price':price})
        price=0
    return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request,book_id):
    cart = request.session.get('cart', {})
    book_id = str(book_id)
    cart.pop(book_id, None)
    request.session['cart'] = cart
    return redirect('cart_view')

def update_cart(request,book_id):
    if request.method == "POST":
        cart = request.session.get('cart', {})
        quantity = int(request.POST.get('quantity', 0))
        book = get_object_or_404(Book, id=book_id)
        if quantity > 0 and quantity <= book.stock:
            cart[book_id] = quantity
        else:
            cart.pop(book_id, None)
        request.session['cart'] = cart
    return redirect('cart_view')       

@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if request.method == "POST" and cart:
      order = Order.objects.create(user=request.user)  
      for book_id, quantity in cart.items():
        book = get_object_or_404(Book, id=book_id)
        OrderItem.objects.create(order=order, book=book, quantity=quantity)
        book.stock -= quantity
        book.save()
      request.session['cart'] = {}
      return redirect('order_history') 
    cart_items=[]
    price = 0
    total_price = 0
    for book_id, quantity in cart.items():
        book = get_object_or_404(Book, id=book_id)
        price= book.price * quantity
        total_price += price
        cart_items.append({'book': book, 'quantity': quantity ,'price':price})
        price=0
    return render(request, 'shop/checkout.html', {'cart_items': cart_items ,'total_price':total_price})
    

@login_required
def order_history(request):
    price = 0
    order_data = []
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    for order in orders:
        items = []
        for item in order.order_items.all():
            price = item.quantity * item.book.price
            items.append({'book': item.book, 'quantity': item.quantity, 'price': price})
            price = 0
        order_data.append({'items': items ,'order': order})
    return render(request, 'shop/order_history.html', {'order_data': order_data})

class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm 
    template_name = 'shop/password_change.html'
    success_url = reverse_lazy('password_change_done')
    

def password_change_done(request):
    return render(request, 'shop/password_change_done.html')

class CustomPasswordResetView(PasswordResetView,LoginRequiredMixin):
    form_class = CustomPasswordResetForm
    template_name = 'shop/password_reset.html'
    
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'shop/password_reset_done.html'

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = 'shop/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'shop/password_reset_complate.html'


def search_books(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request, 'shop/book_list.html', {'books': books, 'query': query})