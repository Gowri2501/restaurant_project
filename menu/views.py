
from django.shortcuts import render, redirect
from .forms import MenuItemForm, OrderForm
from .models import MenuItem, Order

def home(request):
    items = MenuItem.objects.all()

    # MenuItem Form (admin or quick add)
    if request.method == 'POST' and 'add_item' in request.POST:
        menu_form = MenuItemForm(request.POST)
        if menu_form.is_valid():
            menu_form.save()
            return redirect('home')
    else:
        menu_form = MenuItemForm()

    # Order Form
    if request.method == 'POST' and 'place_order' in request.POST:
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()
            return redirect('home')
    else:
        order_form = OrderForm()

    orders = Order.objects.all()

    return render(request, 'menu/home.html', {
        'items': items,
        'menu_form': menu_form,
        'order_form': order_form,
        'orders': orders
    })