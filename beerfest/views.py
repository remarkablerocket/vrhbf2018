from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Beer, UserBeer


@login_required
def user_profile(request):
    beer_list = Beer.objects.filter(
        Q(userbeer__user=request.user, userbeer__starred=True) |
        Q(userbeer__user=request.user, userbeer__tried=True) |
        Q(userbeer__user=request.user, userbeer__rating__isnull=False)
    ).distinct()

    context = {"user": request.user, "beer_list": beer_list}
    return render(request, "beerfest/user_profile.html", context)


@login_required
def star_beer(request, id):
    beer = get_object_or_404(Beer, id=id)
    try:
        userbeer = UserBeer.objects.get(user=request.user, beer=beer)
    except UserBeer.DoesNotExist:
        userbeer = UserBeer(user=request.user, beer=beer)
    else:
        userbeer.starred = True
    userbeer.save()

    return HttpResponse(status=204)


@login_required
def unstar_beer(request, id):
    beer = get_object_or_404(Beer, id=id)
    userbeer = get_object_or_404(UserBeer, user=request.user, beer=beer)
    userbeer.starred = False
    userbeer.save()
    return HttpResponse(status=204)


def index(request):
    return HttpResponseRedirect(reverse("beer_list"))


def beer_list(request):
    beer_list = Beer.objects.order_by("bar__id", "brewery__name", "name")
    context = {"beer_list": beer_list}
    return render(request, "beerfest/beer_list.html", context)


def beer_detail(request, id):
    beer = get_object_or_404(Beer, id=id)
    context = {"beer": beer}
    return render(request, "beerfest/beer_detail.html", context)
