from django.test import TestCase,Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Book, User, Order, OrderItem
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import RequestFactory

# Create your tests here.

User = get_user_model()

class ShopTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='testuser', password='12345',)
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            price=1000,
            stock=10,
            description='A test book description'
        )
        self.order = Order.objects.create(user=self.user, status='pending')
        self.order_item = OrderItem.objects.create(order=self.order, book=self.book, quantity=2)

    def add_session_to_request(self, request):
        middleware = SessionMiddleware(lambda x: None)
        middleware.process_request(request)
        request.session.save()
        return request

    def test_book_model(self):
        self.assertEqual(str(self.book), 'Test Book')
        self.assertEqual(self.book.price, 1000)

    def test_order_model(self):
        self.assertEqual(str(self.order), f"سفارش {self.order.id} - testuser")
        self.assertEqual(self.order.total_price(), 2000)

    def test_order_item_model(self):
        self.assertEqual(str(self.order_item), '2 x Test Book')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/book_list.html')
        self.assertContains(response, 'Test Book')
    
    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/book_detail.html')
        self.assertContains(response, 'Test Author')

    def test_signup_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/signup.html')
        data = {
            'username': 'newuser',
            'password1': 'newpass123',
            'password2': 'newpass123',
            'email':'Test@gmail.com'
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)
        date = {'username': 'testuser', 'password': '12345'}
        response = self.client.post(reverse('login'), date)
        self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_cart_view_and_add_to_cart(self):
        response = self.client.get(reverse('cart_view'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('add_to_cart', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(self.book.id), self.client.session['cart'])
    
    def test_update_cart_view(self):
        self.client.login(username='testuser', password='12345')
        session = self.client.session
        session['cart'] = {str(self.book.id): 2}
        session.save()
        response = self.client.post(reverse('update_cart', args=[self.book.id]), {'quantity': '3'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session['cart'][str(self.book.id)], 3)
        
    def test_remove_from_cart_view(self):
        session = self.client.session
        session['cart'] = {str(self.book.id): 2}
        session.save()
        response = self.client.get(reverse('remove_from_cart', args=[self.book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(str(self.book.id), self.client.session['cart'])

    def test_checkout_view(self):
        self.client.login(username='testuser', password='12345')
        session = self.client.session
        session['cart'] = {str(self.book.id): 2}
        session.save()
        response = self.client.get(reverse('checkout'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('checkout'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Order.objects.filter(user=self.user).exists())

    def test_order_history_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('order_history'))
        self.assertEqual(response.status_code, 200)
        
    def test_password_change_view(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('password_change'))
        self.assertEqual(response.status_code, 200)
        data = {
            'old_password': '12345',
            'new_password1': 'newpass456',
            'new_password2': 'newpass456'
        }
        response = self.client.post(reverse('password_change'), data)
        self.assertEqual(response.status_code, 302)
        self.client.logout()
        self.assertTrue(self.client.login(username='testuser', password='newpass456'))

    def test_password_reset_view(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/password_reset.html')

    def test_search_books_view(self):
        response = self.client.get(reverse('search_books'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')
        response = self.client.get(reverse('search_books'), {'q': 'Nothing'})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Test Book')