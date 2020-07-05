from django.db import models
from shop.models import Product


class Cake(models.Model):
    title = models.CharField(max_length=70, blank=True, verbose_name=u"Название")
    price = models.CharField(max_length=25, blank=True, verbose_name=u"Цена")
    slug = models.SlugField(blank=True, verbose_name=u"Артикул")
    body = models.TextField(max_length=150, blank=True, verbose_name=u"Аннотация")
    drop_body = models.TextField(max_length=350, blank=True, verbose_name=u"Описание")
    image = models.ImageField(blank=True)
    parent = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Торт'
        verbose_name_plural = 'Торты'


    def __str__(self):
        return self.title


class CupCake(models.Model):
    title = models.CharField(max_length=70, blank=True, verbose_name=u"Название")
    price = models.CharField(max_length=25, blank=True, verbose_name=u"Цена")
    slug = models.SlugField(blank=True, verbose_name=u"Артикул")
    body = models.TextField(max_length=150, blank=True, verbose_name=u"Аннотация")
    drop_body = models.TextField(max_length=350, blank=True, verbose_name=u"Описание")
    image = models.ImageField(blank=True)
    parent = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Капкейк'
        verbose_name_plural = 'Капкейки'
