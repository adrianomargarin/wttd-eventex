from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Speaker
from eventex.core.models import Contact


class ContactModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Adriano Margarin',
            slug='adriano-margarin',
            photo='http://hbn.link/hb-pic'
        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='adriano@adriano.com')

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='54-912345678')

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contat kind should be limited to E or P"""
        contact = Contact.objects.create(speaker=self.speaker, kind='A', value='B')

        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='adriano@adriano.com')

        self.assertEqual(str(contact), 'adriano@adriano.com')


class ContactManagerTest(TestCase):

    def setUp(self):
        speaker = Speaker.objects.create(name='Adriano Margarin',
                                         slug='adriano-margarin',
                                         photo='http://hbn.link/hb-pic')

        speaker.contact_set.create(kind=Contact.EMAIL, value='adriano@adriano.com')
        speaker.contact_set.create(kind=Contact.PHONE, value='54-912345678')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['adriano@adriano.com']

        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['54-912345678']

        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
