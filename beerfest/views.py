from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Beer


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
