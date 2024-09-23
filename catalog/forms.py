from django import forms
from .models import Product, Version

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        forbidden_words = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево',
            'бесплатно', 'обман', 'полиция', 'радар'
        ]

        for word in forbidden_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError(
                    f'Название или описание продукта не должно содержать слово "{word}"'
                )

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['product', 'version_number', 'version_name', 'is_current']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        product = cleaned_data.get('product')
        version_number = cleaned_data.get('version_number')
        is_current = cleaned_data.get('is_current')


        if Version.objects.filter(product=product, version_number=version_number).exists():
            raise forms.ValidationError(
                f'Версия с номером {version_number} для этого продукта уже существует.'
            )


        if is_current and Version.objects.filter(product=product, is_current=True).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(
                "Для этого продукта уже есть установленная текущая версия. Сначала сбросьте статус текущей версии для другой версии."
            )

        return cleaned_data
