from django import template
#from messages.models import Messages

register = template.Library()

@register.simple_tag(name='space_single')
def space_single(a, **kwargs):
    b = kwargs['first_mes_level']
    return (a-b)*15


