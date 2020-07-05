from django.shortcuts import render, HttpResponse
from .models import BasePage
from packages.models import Cake, CupCake


def index(request):
    date = BasePage.objects.all()
    return render(request, 'bases.html', context={'date': date})


def index_de_scripts(request):
    if request.method == 'POST':
        model_id = request.POST["id"]
        date = BasePage.objects.get(id=model_id)
        return render(request, 'description/base.html', context={'date': date})


# Упаковка
def cake(request):
    date = Cake.objects.all()
    return render(request, 'cakes.html', context={'date': date})


def cake_de_scripts(request):
    if request.method == 'POST':
        model_id = request.POST["id"]
        date = Cake.objects.get(id=model_id)
        return render(request, 'description/cake.html', context={'date': date})


def cupcake(request):
    date = CupCake.objects.all()
    return render(request, 'cupcakes.html', context={'date': date})


def cupcake_de_scripts(request):
    if request.method == 'POST':
        model_id = request.POST["id"]
        date = CupCake.objects.get(id=model_id)
        return render(request, 'description/cupcake.html', context={'date': date})