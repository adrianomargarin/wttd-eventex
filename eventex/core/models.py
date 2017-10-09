from django.db import models
from django.shortcuts import resolve_url as r

from eventex.core.managers import KindQuerySet
from eventex.core.managers import PeriodManager


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
        (EMAIL, 'E-mail'),
        (PHONE, 'Telefone')
    )

    speaker = models.ForeignKey(Speaker, verbose_name='Palestrante')
    kind = models.CharField(verbose_name='Tipo', max_length=1, choices=KINDS)
    value = models.CharField(verbose_name='Valor', max_length=255)

    objects = KindQuerySet.as_manager()

    def __str__(self):
        return self.value


class Activity(models.Model):

    class Meta:
        abstract = True
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'

    title = models.CharField(verbose_name='Título', max_length=200)
    start = models.TimeField(verbose_name='Início', blank=True, null=True)
    description = models.TextField(verbose_name='Descrição', blank=True)
    speakers = models.ManyToManyField(Speaker,verbose_name='Palestrantes', blank=True)

    objects = PeriodManager()

    def __str__(self):
        return self.title


class Talk(Activity):

    class Meta:
        verbose_name = 'Palestra'
        verbose_name_plural = 'Palestras'

    pass


class Course(Activity):

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    slots = models.IntegerField()
