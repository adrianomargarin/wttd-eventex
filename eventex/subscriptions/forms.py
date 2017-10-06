
from django import forms
from django.core.exceptions import ValidationError

from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionForm(forms.ModelForm):

    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean_name(self):
        return ' '.join(word.capitalize() for word in self.cleaned_data['name'].split())

    def clean(self):
        self.cleaned_data = super().clean()

        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        if not email and not phone:
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data
