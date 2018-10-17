from django import template

register = template.Library()


@register.filter
def nullable_number(value):
    if value is None:
        return ""
    else:
        return value


@register.filter
def abv(value):
    if value is None:
        return ""

    s = str(value)
    return s[:-1] + "." + s[-1:] + "%"
