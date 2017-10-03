# -*- coding:utf-8 -*-

from django.test import TestCase
from django.shortcuts import resolve_url as r

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):

    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Adriano Margarin',
            cpf='12345678901',
            email='adriano@adriano.com',
            phone='54123456789'
        )
        self.response = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        self.assertIsInstance(self.response.context['subscription'], Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.response, expected)


class SubscriptionDetailNotFound(TestCase):

    def setUp(self):
        self.response = self.client.get(r('subscriptions:detail', 0))

    def test_not_found(self):
        self.assertEqual(404, self.response.status_code)
