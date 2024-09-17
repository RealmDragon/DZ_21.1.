from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        prohibited_names = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                            'радар']
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data.lower() in prohibited_names:
            raise forms.ValidationError('Ошибка! Недопустимое название товара!')

        return cleaned_data
