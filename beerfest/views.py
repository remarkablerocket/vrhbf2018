from django.shortcuts import render


from .models import Beer

def beer_list(request):
    beer_list = Beer.objects.order_by("bar__id", "brewery__name", "name")
    context = {"beer_list": beer_list}
    return render(request, "beerfest/index.html", context)
