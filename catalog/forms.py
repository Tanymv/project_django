from django import forms

from catalog.models import Product, Version


class StileFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_title(self):
        cleaned_title = self.cleaned_data['title'].lower()
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in cleaned_title:
                raise forms.ValidationError(f'В названии продукта не должно быть слова {word}')
        return cleaned_title

    def clean_description(self):
        cleaned_description = self.cleaned_data['description'].lower()
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in cleaned_description:
                raise forms.ValidationError(f'В описании продукта не должно быть слова {word}')
        return cleaned_description



class VersionForm(StileFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'