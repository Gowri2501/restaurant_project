from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    menu_items = models.ManyToManyField(MenuItem)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return sum(item.price for item in self.menu_items.all())

    def __str__(self):
        return f"Order by {self.customer_name}"
