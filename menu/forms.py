from django import forms
from .models import MenuItem, Order

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'description', 'price']

class OrderForm(forms.ModelForm):
    menu_items = forms.ModelMultipleChoiceField(
        queryset=MenuItem.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Order
        fields = ['customer_name', 'menu_items']