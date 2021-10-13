from django.urls import path

from .views import PageListView, PageDetailView

urlpatterns = [
    path('content/', PageListView.as_view(), name='list_content'),
    path('content/<int:pk>/', PageDetailView.as_view(), name='detail_content')
]
