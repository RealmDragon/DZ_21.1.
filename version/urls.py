from django.urls import path
from version.apps import VersionConfig
from version.views import VersionListView, VersionCreateView

# VersionUpdateView, VersionDeleteView, VersionDetailView

app_name = VersionConfig.name

urlpatterns = [
    path('', VersionListView.as_view(), name='version_list'),
    path('version/create/', VersionCreateView.as_view(), name='version_create'),
]
# path('version/<int:pk>/', VersionDetailView.as_view(), name='version_detail'),
# path('version/update/<int:pk>/', VersionUpdateView.as_view(), name='version_update'),
# path('version/delete/<int:pk>/', VersionDeleteView.as_view(), name='version_delete'),
