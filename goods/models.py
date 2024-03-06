from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    # Меняем имя на русское, для одного товара и несколько
    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
        ordering = ("id",)

    # Меняет название на нормальное
    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="goods_images", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, verbose_name="Цена"
    )
    discount = models.DecimalField(
        default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка в %"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        to=Categories, on_delete=models.CASCADE, verbose_name="Категория"
    )

    # Меняем имя на русское, для одного товара и несколько
    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    # Меняет название на нормальное + добавляет количество
    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
    # Вызывает id, плюс, через 06, добавляет нолики перед числом, получаем например 00001
    def display_id(self):
        return f"{self.id:06}"

    # Метод проверяет есть ли скидка, и возвращает цену минус скидка, или цену,
    # округляем до 2 знака после запятой
    def self_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
