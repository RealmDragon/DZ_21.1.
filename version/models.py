from django.db import models

from catalog.models import Product


class Version(models.Model):
    product = models.ForeignKey(Product,
                                related_name="versions",
                                verbose_name="Продукт",
                                help_text="продукт, к которому принадлежит версия",
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True,
                                )
    version_number = models.PositiveIntegerField(
        default=0,
        verbose_name="Номер версии",
        help_text="номер версии",
    )
    version_name = models.CharField(
        max_length=50,
        verbose_name="Название версии",
        help_text="название версии",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Текущая версия",
    )

    def __str__(self):
        return f"{self.version_number} {self.version_name} {self.is_active}"

    class Meta:
        verbose_name = "версия продукта"
        verbose_name_plural = "версии продуктов"
