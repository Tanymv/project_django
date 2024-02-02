from django.db import models
NULLABLE = {"blank": True, "null": True}

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="заголовок")
    slug = models.CharField(max_length=150, **NULLABLE, verbose_name="slug")
    body = models.TextField(max_length=150, **NULLABLE, verbose_name="содержимое")
    image = models.ImageField(upload_to="catalog/", **NULLABLE, verbose_name="превью")
    date_creation = models.DateTimeField(**NULLABLE, verbose_name="дата создания")
    sign_publication = models.CharField(max_length=150, verbose_name="признак публикации")
    number_views = models.IntegerField(default=0, verbose_name="количество просмотров")

    views_count = models.IntegerField(default=0, verbose_name='просмотры')
    is_published = models.BooleanField(default=True, verbose_name='положительно опубликованы')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.title} {self.slug}'

    class Meta:
        verbose_name = 'статья'  # Настройка для наименования одного объекта
        verbose_name_plural = 'статьи'  # Настройка для наименования набора объектов