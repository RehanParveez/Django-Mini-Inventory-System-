from django.test import TestCase
from django.urls import reverse
from django.db.models import Sum
from Student.models import Products

# Create your tests here.

class ProductTests(TestCase):
    
    def setup(self):
       self.p1 = Products.objects.create(name='Pen', quantity='10', category='Stationery')
       self.p2 = Products.objects.create(name='Marker', quantity='3', category='Stationery')
      
    def test_total_quantity(self):
        total = Products.objects.aggregate(total=Sum('quantity'))['total']
        self.assertEqual(total, 13)
        
    def test_low_stock_filter(self):
        low_stock_items = Products.objects.filter(quantity__lt=5)
        self.assertIn(self.p2, low_stock_items)
        self.assertNotIn(self.p1, low_stock_items)
        
    def test_sell_product(self):
        url = reverse('sell_product', args=[self.p1.id])
        self.client.post(url, {'amount': 2})
        self.p1.refresh_from_db()
        self.assertEqual(self.p1.quantity, 8)
        
        
        
        
        
        
