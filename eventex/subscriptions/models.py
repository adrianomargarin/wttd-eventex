# -*- coding:utf-8 -*-

from django.db import models


class Subscription(models.Model):

    class Meta:
        verbose_name = 'Inscrição'
        verbose_name_plural = 'Inscrições'
        ordering = ['-created_at']

    name = models.CharField('Nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11)
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone', max_length=20)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    paid = models.BooleanField(verbose_name='Pago', default=False)

    def __str__(self):
        return self.name
