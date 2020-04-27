from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """
    Function cuts all arg from value string.
    """
    return value.replace(arg, '')

# register.filter('cut',cut)
