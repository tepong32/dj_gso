from django import template

register = template.Library()

@register.filter
def model_fields(model_instance):
    return model_instance._meta.fields

@register.filter
def get_attr(obj, attr):
    return getattr(obj, attr)
