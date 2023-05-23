from django import template

register = template.Library()

@register.filter
def get_attribute(model, field_name):
    try:
        return getattr(model, field_name)
    except:
        return None