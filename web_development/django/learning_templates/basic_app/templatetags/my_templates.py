from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

#register.filter('cut', cut)

@register.filter('replace_to_ben')
def replace_to_ben(value, arg):
    """
    Custom template filter replace to my name.
    """
    return value.replace(arg,'ben')
