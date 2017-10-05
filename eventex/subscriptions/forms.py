

from django import forms
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números', 'length')


class SubscriptionForm(forms.Form):

    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        return ' '.join(word.capitalize() for word in self.cleaned_data['name'].split())

    def clean(self):
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')

        if not email and not phone:
            raise ValidationError('Informe seu e-mail ou telefone.')

        return self.cleaned_data
