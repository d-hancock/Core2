from django import forms
from shop.models import Shop
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class ShopForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'url']
