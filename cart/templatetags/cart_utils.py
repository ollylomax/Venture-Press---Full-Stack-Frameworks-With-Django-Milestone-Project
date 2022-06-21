from django import template

register = template.Library()

@register.filter(name='calculate_sub')
def calculate_sub(price, quantity):
    return price * quantity