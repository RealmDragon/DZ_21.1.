from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        """
        Привязываем созданный продукт к текущему пользователю.
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'  # Указываем имя переменной для шаблона

    def get_queryset(self):
        """
        Получаем только продукты текущего пользователя.
        """
        return Product.objects.filter(owner=self.request.user)


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    context_object_name = 'product'  # Указываем имя переменной для шаблона


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            print(f'{name} ({phone}): {message}')
        return render(request, 'catalog/contacts.html')


# CRUD для Версий
class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')  # Перенаправляем на список продуктов

    def form_valid(self, form):
        product_id = self.kwargs['product_id']
        product = Product.objects.get(pk=product_id)
        form.instance.product = product
        return super().form_valid(form)


class VersionUpdateView(LoginRequiredMixin, UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:product_list')  # Перенаправляем на список продуктов

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.product.pk})


class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:product_list')  # Перенаправляем на список продуктов

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk': self.object.product.pk})
