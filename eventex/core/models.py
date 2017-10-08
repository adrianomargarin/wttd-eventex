from django.db import models
from django.shortcuts import resolve_url as r


class Speaker(models.Model):

    class Meta:
        verbose_name = 'Palestrante'
        verbose_name_plural = 'Palestrantes'

    name = models.CharField(verbose_name='Nome', max_length=255)
    slug = models.SlugField(verbose_name='Slug')
    photo = models.URLField(verbose_name='Foto')
    website = models.URLField(verbose_name='Website', blank=True)
    description = models.TextField(verbose_name='Descrição', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    EMAIL = 'E'
    PHONE = 'P'

    KINDS = (
        ('E', EMAIL),
        ('P', PHONE)
    )

    speaker = models.ForeignKey(Speaker, verbose_name='Palestrante')
    kind = models.CharField(verbose_name='Tipo', max_length=1, choices=KINDS)
    value = models.CharField(verbose_name='Valor', max_length=255)

    def __str__(self):
        return self.value


class Talk(models.Model):

    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'

    title = models.CharField(verbose_name='Título', max_length=200)
    start = models.TimeField(verbose_name='Início', blank=True, null=True)
    description = models.TextField(verbose_name='Descrição', blank=True)
    speakers = models.ManyToManyField(Speaker,verbose_name='Palestrantes', blank=True)

    def __str__(self):
        return self.title
