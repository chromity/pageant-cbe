from django.shortcuts import render
from candidates.models import *
from .forms import PrePageantForm
from django.shortcuts import redirect, get_object_or_404


def index(request):
    context = {

    }

    return render(request, 'candidates/index.html', context)


def pre_pageant_list(request):
    data = PrePageant.objects.filter(judge=request.user).order_by('total')
    return render(request, 'candidates/pre_pageant_list.html', {'data': data})


def pre_pageant_detail(request):
    return render(request, 'candidates/pre_pageant_detail.html')


def pre_pageant_add(request):
    if request.method == "POST":
        form = PrePageantForm(request.POST)

        if form.is_valid():
            prepageant = form.save(commit=False)
            prepageant.judge = request.user
            prepageant.total = float(
                        form.talent / 100.0000 * 30 +
                        form.essay / 100.0000 * 30 +
                        form.corporate_attire / 100.0000 * 20 +
                        form.panel_interview / 100.0000 * 20)
            prepageant.save()
            return redirect('pre_pageant_detail', pk=prepageant.pk)
    else:
        form = PrePageantForm
        return render(request, 'candidates/pre_pageant_add.html', {'form': form})


def pre_pageant_edit(request, pk):
    prepageant = get_object_or_404(PrePageant, pk=pk)

    if request.method == "POST":
        form = PrePageantForm(request.POST, instance=PrePageant)

        if form.is_valid():
            prepageant = form.save(commit=False)
            prepageant.judge = request.user
            prepageant.total = float(
                form.talent / 100.0000 * 30 +
                form.essay / 100.0000 * 30 +
                form.corporate_attire / 100.0000 * 20 +
                form.panel_interview / 100.0000 * 20)
            prepageant.save()
            return redirect('pre_pageant_detail', pk=prepageant.pk)
    else:
        form = PrePageantForm(instance=PrePageant)
        return render(request, 'candidates/pre_pageant_edit.html', {'form': form})
