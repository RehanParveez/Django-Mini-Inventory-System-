from django.urls import path
from Student.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, OwnLoginView, OwnLogoutView, RegisterationView, SellProductView, LowStockView, DashboardView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('productdetail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('productcreate/', ProductCreateView.as_view(), name='product_create'),
    path('productupdate/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('productdelete<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('productsell/<int:pk>/', SellProductView.as_view(), name='sell_product'),
    path('lowstock/', LowStockView.as_view(), name='low_stock'),
    
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('login/',OwnLoginView.as_view(), name='login'),
    path('logout/', OwnLogoutView.as_view(), name='logout'),
    path('register/', RegisterationView.as_view(), name='register')
]
