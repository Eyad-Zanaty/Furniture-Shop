from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Adds a CSS class to a form field."""
    field.field.widget.attrs["class"] = css_class
    return field

@register.filter(name='add_placeholder')
def add_placeholder(field, placeholder):
    """Adds a placeholder attribute to a form field."""
    field.field.widget.attrs["placeholder"] = placeholder
    return field
