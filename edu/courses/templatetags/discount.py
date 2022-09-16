from django import template

register = template.Library()
@register.filter
def dis(price,discount):
    price = int(price)
    discount = int(discount)
    return str(price - (discount/100)*price)
