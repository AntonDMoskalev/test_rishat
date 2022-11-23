from django import forms
from django.contrib import admin
from items.models import Discount, Item, Order, Tax


class ItemAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "сurrency")
    search_fields = ("name",)
    list_filter = ("id",)
    empty_value_display = "-pass-"


class TaxCreateForm(forms.ModelForm):
    """
    Custom Tax creation form, removed tax_rate(created automatically).
    """
    class Meta:
        model = Tax
        fields = ["name", "inclusive", "percentage", "description"]


class TaxAdmin(admin.ModelAdmin):
    form = TaxCreateForm
    list_display = ("id", "name", "inclusive",
                    "percentage", "description", "tax_rate")
    search_fields = ("name",)
    list_filter = ("id",)
    empty_value_display = "-pass-"


class DiscountAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "percent_off", "duration")
    search_fields = ("name",)
    list_filter = ("id",)
    empty_value_display = "-pass-"


admin.site.register(Item, ItemAdmin)
admin.site.register(Tax, TaxAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Order)
