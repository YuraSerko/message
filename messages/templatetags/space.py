from django import template
#from messages.models import Messages

register = template.Library()

@register.simple_tag(name='space')
def space(a):
    return a*15


#register.simple_tag(current_time)