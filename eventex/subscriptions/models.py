
from django.db import models
from eventex.subscriptions.validators import validate_cpf


class Subscription(models.Model):

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ['-created_at']

    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('E-mail', blank=True)
    phone = models.CharField('Telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    paid = models.BooleanField(verbose_name='Pago', default=False)

    def __str__(self):
        return self.name
