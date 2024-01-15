from django.db import models

# Create your models here.
NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(max_length=150, **NULLABLE, verbose_name="описание")
    created_at = models.CharField(**NULLABLE)

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="наименование")
    description = models.TextField(max_length=150, **NULLABLE, verbose_name="описание")
    image = models.ImageField(upload_to="catalog/", **NULLABLE, verbose_name="изображение")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="категория")
    price = models.IntegerField(verbose_name="цена за штуку")
    date_creation = models.DateTimeField(**NULLABLE, verbose_name="дата создания")
    last_modified_date = models.DateTimeField(**NULLABLE, verbose_name="дата последнего изменения")

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name} {self.description}'

    class Meta:
        verbose_name = 'продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'продукты'  # Настройка для наименования набора объектов
