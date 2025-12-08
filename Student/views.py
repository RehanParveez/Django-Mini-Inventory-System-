
# Python Test part

# Problem 1. Write a program to take user input amount and check check that how many currency notes contains that amount.

# like notes 5000, 1000, 500, 100, 50, 20, 10, 5, 2,1

# amount = input('enter your decideamount')
# currency = ['1000', '500', '100', '50', '20', '10', '5', '2','1']
# for i in currency:
#     result = amount // i
#     print(result)


# Correct

# currency = ['5000', '1000', '500', '100', '50', '20', '10', '5', '2', '1']
# amount = int(input("Enter you amount"))

# for i in currency:
#     result = amount // currency
#     print(f"{i} = {result}")
#     amount = amount % i


    

    


# Problem 2: Filter and Validate Matrix Rows
# Statement:
# You are given a 4×4 matrix. Check each row to ensure all values lie between 1 and 100.
# Then, filter out the rows where the sum of the elements is less than 150.
# Finally, return the valid and filtered rows sorted in descending order of their row sums.

# list_2d44 = [
#     [1, 2, 3, 4]
#     [5, 6, 7, 8]
#     [9, 10, 11, 12]
#     [13, 14, 15, 16]
# ]

# rows = []
# sum = []

# for i in list_2d44:    
#     if all(0<=j<100 for j in i):
#         rows += i
#     for i in list_2d44:
#       if all(sum(i) >= 150):
#          i >= 150
#          sum += 1
#     else:
#         raise ValueError("Invalid matrix, element should be between 0 to 100 ")
# print(reversed(rows))


# Correct

# rows = []

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]

# for i in matrix:
#     if all(1 <= j <= 100 for j in i):
#         if sum(i) >= 150:
#             rows.append(i)
#     else:
#         raise ValueError('Invalid matrix, enter element between 1 and 100')
    
# rows.sort(key=sum, reverse=True)


    

# Problem 3: Group Anagrams
# Given a list of strings, group the strings that are anagrams of each other.

# Example:
# Input: ["eat","tea","tan","ate","nat","bat"]

# Output:
# [
#   ["eat","tea","ate"],
#   ["tan","nat"],
#   ["bat"]
# ]



# from collections import defaultdict
# words = ["eat","tea","tan","ate","nat","bat"]

# for i in words:
#   merge = defaultdict(list)
#   alphabet = ''. join(sorted(i))
#   merge[alphabet].append[i]

# result = list(merge.i)
# print(result)


# Correct

# from collections import defaultdict

# words = ["eat","tea","tan","ate","nat","bat"]
# merge = defaultdict(list)

# for i in words:
#     alphabet = ''.join(sorted(i))
#     merge = [alphabet].append(i)
    
# result = list(merge.values())
# print(result)
    











# Django Test Part


# Create your views here.

# Django Questions:

# Mini Inventory System

# Requirements:

# Products: name, quantity, category

# CRUD for products

# Decrease quantity when “sold”

# Show low-stock items (<5 quantity)

# Dashboard page showing stats

# Tests: Aggregation, filtering, business logic.

from django.shortcuts import render, redirect, get_object_or_404
from Student.forms import ProductForm, RegisterForm
from Student.models import Products
from django.contrib.auth import views
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.db.models import Sum
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LogoutView




class RegisterationView(View):
    template_name = 'Student/register.html'
    
    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            form = RegisterForm()
            return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
        return render(request, self.template_name, {'form': form})
    



class OwnLoginView(View):
    template_name = 'Student/login.html'
    
    def get(self ,request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data = request.POST)
    
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('product_list')
        return render(request, self.template_name, {'form': form})
    

class OwnLogoutView(LogoutView):
    next_page = 'product_list'
    template_name = 'Student/logout.html'



class ProductListView(ListView):
    model = Products
    template_name = 'Student/product_list.html'
    context_object_name = 'products'
    

class ProductDetailView(DetailView):
    model = Products
    template_name = 'Student/product_detail.html'
    context_object_name = 'product'
    

class ProductCreateView(CreateView):
    model = Products
    fields = ['name', 'quantity', 'category',]
    template_name = 'Student/product_create.html'
    success_url = reverse_lazy('product_list')
    
    
class ProductUpdateView(UpdateView):
    model = Products
    fields = ['name', 'quantity', 'category']
    template_name = 'Student/product_update.html'
    success_url = reverse_lazy('product_list')
    
    
class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'Student/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')
    

class SellProductView(View):
    def post(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        amount = int(request.POST.get('amount', 1))
        
        if 0 < amount <= product.quantity:
            product.quantity -= amount
            product.save()
            messages.success(request, "product sold successfully")
        else:
            messages.error(request, 'invalid quantity')
    
        return redirect('product_detail', pk=pk)
    

class LowStockView(View):
    model = Products
    template_name = 'Student/product_low_stock.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Products.objects.filter(quantity__lt=5)
    
    def get(self, request):
        products = self.get_queryset()
        return render(request, self.template_name, {self.context_object_name: products})
    

class DashboardView(TemplateView):
    template_name = 'Student/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['total_products'] = Products.objects.count()
        context['low_stock'] = Products.objects.filter(quantity__lt=5).count()
        context['total_quantity'] = Products.objects.aggregate(total=Sum('quantity'))['total'] or 0
        return context
    
    
    

