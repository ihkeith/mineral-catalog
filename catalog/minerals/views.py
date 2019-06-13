from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

import random

from .models import Mineral

# Create your views here.
def index(request):
    # return redirect(mineral_list)
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    try:
        mineral = get_object_or_404(Mineral, pk=pk)
    except Mineral.DoesNotExist:
        raise Http404("Page does not exist!")
    else:
        return render(request, 'minerals/mineral_detail.html', {'mineral': mineral})
