from core.models import SalesOrder, Customer, Company

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from customer.serializers import SalesOrderSerializer

SALESORDER_URL = reverse("customer:salesorder-list")


class PublicSalesOrderApiTest(TestCase):
    """Test the publicly available salesorder API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retreiving invoices"""
        res = self.client.get(SALESORDER_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateSalesOrderApiTest(TestCase):
    """Test authorized user SalesOrder API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test@crownkiraappdev.com",
            "password123",
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retreive_salesorder(self):
        """Test retreiving salesorder"""
        testcompany = Company.objects.create(name='testcompany')
        testcustomer = Customer.objects.create(
            company=testcompany, name='testcustomer',
        )
        testcustomer2 = Customer.objects.create(
            company=testcompany, name='testcustomer2',
        )
        SalesOrder.objects.create(
            company=testcompany,
            customer=testcustomer,
            salesperson=self.user,
            date="2001-01-10",
            payment_date="2001-01-10",
            gst_rate="0.07",
            discount_rate="0",
            gst_amount="0",
            discount_amount="0",
            net="0",
            total_amount="0",
            grand_total="0",
        )
        SalesOrder.objects.create(
            company=testcompany,
            customer=testcustomer2,
            salesperson=self.user,
            date="2001-01-10",
            payment_date="2001-01-10",
            gst_rate="0.07",
            discount_rate="0",
            gst_amount="0",
            discount_amount="0",
            net="0",
            total_amount="0",
            grand_total="0",
        )
        res = self.client.get(SALESORDER_URL)

        receives = SalesOrder.objects.all().order_by("id")
        serializer = SalesOrderSerializer(receives, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_salesorder_not_limited_to_user(self):
        """Test that salesorder returned are visible by every user"""
        testuser = get_user_model().objects.create_user(
            "testsales@crownkiraappdev.com" "password1234"
        )
        testcompany = Company.objects.create(name='testcompany')
        testcustomer = Customer.objects.create(
            company=testcompany, name='testcustomer',
        )
        testcustomer2 = Customer.objects.create(
            company=testcompany, name='testcustomer2',
        )
        SalesOrder.objects.create(
            customer=testcustomer,
            salesperson=self.user,
            company=testcompany,
            date="2001-01-10",
            payment_date="2001-01-10",
            gst_rate="0.07",
            discount_rate="0",
            gst_amount="0",
            discount_amount="0",
            net="0",
            total_amount="0",
            grand_total="0",
        )
        SalesOrder.objects.create(
            customer=testcustomer2,
            salesperson=self.user,
            company=testcompany,
            date="2001-01-10",
            payment_date="2001-01-10",
            gst_rate="0.07",
            discount_rate="0",
            gst_amount="0",
            discount_amount="0",
            net="0",
            total_amount="0",
            grand_total="0",
        )
        res = self.client.get(SALESORDER_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

        self.user = testuser
        self.client.force_authenticate(self.user)

        res = self.client.get(SALESORDER_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 2)

    def test_create_salesorder_successful(self):
        """Test creating a new salesorder"""
        self.company = Company.objects.create(name='testcompany')
        self.customer = Customer.objects.create(
            company=self.company, name='testcustomer',
        )
        payload = {
            'customer': self.customer.id,
            'salesperson': self.user,
            'company': self.company.id,
            'date': "2001-01-10",
            'payment_date': "2001-01-10",
            'gst_rate': "0.07",
            'discount_rate': "0",
            'gst_amount': "0",
            'discount_amount': "0",
            'net': "0",
            'total_amount': "0",
            'grand_total': "0",
        }
        self.client.post(SALESORDER_URL, payload)
        exists = SalesOrder.objects.filter(customer=payload["customer"])
        self.assertTrue(exists)

    def test_create_salesorder_invalid(self):
        """Test creating a new supplier with invalid payload"""
        payload = {
            'customer': '',
            'salesperson': self.user,
            'date': "2001-01-10",
            'payment_date': "2001-01-10",
            'gst_rate': "0.07",
            'discount_rate': "0",
            'gst_amount': "0",
            'discount_amount': "0",
            'net': "0",
            'total_amount': "0",
            'grand_total': "0",
        }
        res = self.client.post(SALESORDER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
