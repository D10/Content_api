from rest_framework import generics
from django.db.models import F
from django.db import transaction

from .serializers import PageListSerializer, PageDetailSerializer
from .pagination import ContentPagination
from .models import Page, Content


class PageListView(generics.ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer
    pagination_class = ContentPagination


class PageDetailView(generics.RetrieveAPIView):
    serializer_class = PageDetailSerializer

    @transaction.atomic
    def update_counter(self):
        page_pk = self.kwargs.get('pk')
        content = Content.objects.filter(page__pk=page_pk)
        content.update(counter=F('counter') + 1)

    def get_queryset(self):
        self.update_counter()
        return Page.objects.all()
