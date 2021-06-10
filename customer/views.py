from core.pagination import CustomPagination
from core.views import BaseClassAttrForViewSet
from rest_framework.response import Response
from rest_framework import status

from core.models import Invoice, Customer, SalesOrder

from customer import serializers


class InvoiceViewSet(BaseClassAttrForViewSet):
    """Manage invoice in the database"""
    queryset = Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    pagination_class = CustomPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def perform_create(self, serializer):
        serializer.save()


class CustomerViewSet(BaseClassAttrForViewSet):
    """Manage customer in the database"""
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    pagination_class = CustomPagination


class SalesOrderViewSet(BaseClassAttrForViewSet):
    """Manage customer in the database"""
    queryset = SalesOrder.objects.all()
    serializer_class = serializers.SalesOrderSerializer
    pagination_class = CustomPagination
