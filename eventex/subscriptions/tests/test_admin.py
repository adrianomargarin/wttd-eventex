
from unittest.mock import Mock

from django.test import TestCase
from eventex.subscriptions.admin import admin
from eventex.subscriptions.admin import Subscription
from eventex.subscriptions.admin import SubscriptionModelAdmin


class SubscriptionModelAdminTest(TestCase):

    def setUp(self):
        Subscription.objects.create(name='Adriano Margarin', cpf='12345678901',
                                    email='adriano@margarin.gmail', phone='54-912345678')
        self.model_admin = SubscriptionModelAdmin(Subscription, admin.site)

    def test_has_action(self):
        """Action mark as paid should be installed."""
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        """It should mark all selected subscriptions as paid."""
        self.call_action()

        self.assertEqual(Subscription.objects.filter(paid=True).count(), 1)

    def test_message(self):
        """It should send a message to the user."""
        mock = self.call_action()

        mock.assert_called_once_with(None, '1 inscrição for marcada como paga.')

    def call_action(self):
        queryset = Subscription.objects.all()

        mock = Mock()
        old_message_user = self.model_admin.message_user
        self.model_admin.message_user = mock
        self.model_admin.mark_as_paid(None, queryset)
        self.model_admin.message_user = old_message_user

        return mock
