from django import template

register = template.Library()


@register.filter(name='add_css')
def add_css(field, css):
    u"""Add css class to field."""

    return field.as_widget(attrs={"class": css})
