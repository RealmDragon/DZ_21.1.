from django.db import models


# Create your models here.


# создаем модель категории как одного ко многим
class Category(models.Model):
    # наименование, описание
    name = models.CharField(
        max_length=100, verbose_name="категория", help_text="Введите категорию продукта"
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} {self.description}"



# создаем модель продуктов как многих к одной категории. Ссылка на категорию
# создаем класс и наследуемся от models.Model
class Product(models.Model):
    # имя, порода, фото, дата рождения
    # создаем поля и прописываем их параметры
    name = models.CharField(
        max_length=100,
        verbose_name="наименование",
        help_text="введите наименование продукта",
    )
    description = models.TextField(
        max_length=100, verbose_name="описание", help_text="Введите описание продукта"
    )
    image = models.ImageField(
        upload_to="catalog/image",
        blank=True,
        null=True,
        verbose_name="изображение",
        help_text="загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.PositiveIntegerField(default=0, )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name="дата создания",
        help_text="Укажите дату создания записи в БД",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="дата последнего изменения",
        help_text="Укажите дату изменения записи в БД",
    )

    # Класс мета
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["category", "name"]

    # строковое представление объекта
    def __str__(self):
        return f"{self.name} {self.category} {self.created_at}"

class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="versions")
    version_number = models.CharField(max_length=20)
    version_name = models.CharField(max_length=100)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name} - {self.version_name}"

    def set_current_version(self):
        # Сбросить статус "текущая" для всех других версий этого продукта
        Version.objects.filter(product=self.product, is_current=True).update(is_current=False)
        # Установить текущую версию
        self.is_current = True
        self.save()

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"