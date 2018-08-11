from django.shortcuts import render
from candidates.models import *


def index(request):
    context = {

    }

    return render(request, 'candidates/index.html', context)
