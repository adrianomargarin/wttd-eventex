
from django.test import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        """Form must have have 4 fields"""
        form = SubscriptionForm()
        expect = ['name', 'cpf', 'email', 'phone']

        self.assertSequenceEqual(expect, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must only accept digits."""
        form = self.make_validated_form(cpf='ABCD567901')

        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must 11 digits."""
        form = self.make_validated_form(cpf='1234')

        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """Name must be be capitalize"""
        form = self.make_validated_form(name='ADRIANO margarin')

        self.assertEqual(form.cleaned_data['name'], 'Adriano Margarin')

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(email='')

        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validated_form(phone='')

        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email an Phone are optional, but one must be informed"""
        form = self.make_validated_form(email='', phone='')

        self.assertListEqual(list(form.errors), ['__all__'])

    def test_must_inform_email_incorrect_or_phone(self):
        """Email incorrect an Phone are optional, but one must be informed"""
        form = self.make_validated_form(email='incorrect', phone='')

        self.assertListEqual(list(form.errors), ['__all__', 'email'])

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]

        self.assertEqual(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]

        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = {
            'name': 'Adriano Margarin',
            'cpf': '12345678901',
            'email': 'adriano@margarin.com',
            'phone': '54-912345678'
        }

        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()

        return form
