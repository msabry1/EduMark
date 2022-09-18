from django import template

register = template.Library()
@register.filter
def replace(word):
    return word.replace('\n','<br>')