import stripe
from django.db import models

from rishat_shop.settings import STRIPE_SECRET_KEY

CURRENCY_CHOICES = (
    ("usd", "USD"),
    ("eur", "EUR"),
)

DURATION_CHOICES = (
    ("once", "once"),
    ("repeating", "repeating"),
    ("forever", "forever")
)


class Tax(models.Model):
    """
    Tax calculation model.
    name: Name of the tax.
    inclusive: Is the tax included in the amount or charged.
    percentage: Tax rate as a percentage.
    description: Description of the tax.
    tax_rate(created when saving): Tax key after registration.

    The save method.
    Automatically registers a new tax in the Strip and receives a key.
    """
    name = models.CharField(max_length=50)
    inclusive = models.BooleanField(default=False)
    percentage = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.CharField(max_length=100)
    tax_rate = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        try:
            stripe.api_key = STRIPE_SECRET_KEY
            tax_id = stripe.TaxRate.create(display_name=self.name,
                                           inclusive=self.inclusive,
                                           percentage=self.percentage,
                                           description=self.description)
            self.tax_rate = tax_id.id
            super().save(*args, **kwargs)
        except Exception as e:
            return str(e)

    def __str__(self):
        return self.name


class Item(models.Model):
    """
    Model of items for sale.
    name: Name of the item.
    description: Item description.
    price: Item price.
    сurrency: Settlement currency (usd, eur).
    tax: Item tax.
    """
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    сurrency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    tax = models.ForeignKey(Tax, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class Discount(models.Model):
    """
    Discount model.
    name: Discount name (id).
    description: Description of the discount.
    percent_off: Discount percentage.
    duration: duration of the discount (once, repeating, forever).

    The save method.
    When saving, it is registered in the Strip.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    percent_off = models.DecimalField(max_digits=4, decimal_places=2)
    duration = models.CharField(max_length=11, choices=DURATION_CHOICES)

    def save(self, *args, **kwargs):
        try:
            stripe.api_key = STRIPE_SECRET_KEY
            stripe.Coupon.create(duration=self.duration,
                                 id=self.name,
                                 percent_off=self.percent_off)
            super().save(*args, **kwargs)
        except Exception as e:
            return str(e)

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Product basket model.
    items: Items in the basket.
    discounts: Discounts applied to the shopping cart.
    """
    items = models.ManyToManyField(Item)
    discounts = models.ManyToManyField(Discount)

    def __str__(self):
        return str(self.id)
