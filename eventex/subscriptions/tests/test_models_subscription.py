# -*- coding:utf-8 -*-

from datetime import datetime
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Adriano Margarin',
            cpf='12345678901',
            email='adriano@adriano.com',
            phone='54123456789'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscriptions must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Adriano Margarin', str(self.obj))
