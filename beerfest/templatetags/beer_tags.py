from django import template

from beerfest.models import UserBeer


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
        return "TBC"

    s = str(value)
    return s[:-1] + "." + s[-1:] + "%"


@register.simple_tag
def user_starred_beer(user_id, beer_id):
    return UserBeer.objects.filter(
        user__id=user_id, beer__id=beer_id, starred=True
    )


@register.inclusion_tag("beerfest/beer_list_table.html")
def display_beer_table(beer_list, user):
    return {"beer_list": beer_list, "user": user}
