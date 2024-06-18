from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,get_object_or_404,redirect
from  users.prmissionmixin import SalarRequiredMixin
from  django.views import  View
from .forms import ProductForm
from django.urls import reverse
from users.models import Product,Client,User

class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'salar/products.html', {'products': products})

    
class ProfileViewAdmin(LoginRequiredMixin,View):
    def get(self,request):
        user = request.user
        return render(request,'salar/dashboard.html',context={"user":user})

class Delete(LoginRequiredMixin, View):
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect(reverse('salar:dashboard'))
    
class CreateProductView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'salar/create.html', {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('salar:dashboard')
        return render(request, 'salar/create.html', {'form': form})
    
class EditProfileView(LoginRequiredMixin, View):
    def get(self, request, id):
        product = get_object_or_404(Product,id=id)
        form = ProductForm(instance=product)
        return render(request, 'salar/update.html', {'form': form})

    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/dashboard')  
        return render(request, 'salar/update.html', {'form': form})
    