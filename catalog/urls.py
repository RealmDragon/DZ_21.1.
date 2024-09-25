from django.urls import path
from .views import (
    ProductCreateView, ProductUpdateView, ProductListView,
    ProductDetailView, ProductDeleteView, ContactsTemplateView,
    VersionCreateView, VersionUpdateView, VersionDeleteView
)

app_name = 'catalog'

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),

    # URL для версий
    path('<int:product_id>/version/create/', VersionCreateView.as_view(), name='version_create'),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name='version_update'),
    path('version/<int:pk>/delete/', VersionDeleteView.as_view(), name='version_delete'),
]
