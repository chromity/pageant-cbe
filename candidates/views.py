from django.shortcuts import render
from candidates.models import *
from .forms import PrePageantForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='admin:login')
def index(request):
    context = {

    }

    return render(request, 'candidates/index.html', context)


@login_required(login_url='admin:login')
def pre_pageant_list(request):
    data = PrePageant.objects.filter(judge=request.user).order_by('total')
    return render(request, 'candidates/pre_pageant_list.html', {'data': data})


@login_required(login_url='admin:login')
def pre_pageant_detail(request, pk):
    data = get_object_or_404(PrePageant, pk=pk)
    return render(request, 'candidates/pre_pageant_detail.html', {'data': data})


@login_required(login_url='admin:login')
def pre_pageant_add(request):
    if request.method == "POST":
        form = PrePageantForm(request.POST)

        if PrePageant.objects.get(judge=request.user, candidate__idx=request.POST['candidate']):
            form = PrePageantForm
            return render(request, 'candidates/pre_pageant_add.html', {'form': form})

        if form.is_valid():
            prepageant = form.save(commit=False)
            prepageant.judge = request.user
            prepageant.total = float(
                        prepageant.talent / 100.0000 * 30 +
                        prepageant.essay / 100.0000 * 30 +
                        prepageant.corporate_attire / 100.0000 * 20 +
                        prepageant.panel_interview / 100.0000 * 20)
            prepageant.save()
            return redirect('pre_pageant_detail', pk=prepageant.pk)
    else:
        form = PrePageantForm
        return render(request, 'candidates/pre_pageant_add.html', {'form': form})


@login_required(login_url='admin:login')
def pre_pageant_edit(request, pk):
    prepageant = get_object_or_404(PrePageant, pk=pk)

    if request.method == "POST":
        form = PrePageantForm(request.POST, instance=prepageant)

        if form.is_valid():
            prepageant = form.save(commit=False)
            prepageant.judge = request.user
            prepageant.total = float(
                prepageant.talent / 100.0000 * 30 +
                prepageant.essay / 100.0000 * 30 +
                prepageant.corporate_attire / 100.0000 * 20 +
                prepageant.panel_interview / 100.0000 * 20)
            prepageant.save()
            return redirect('pre_pageant_detail', pk=prepageant.pk)
    else:
        form = PrePageantForm(instance=prepageant)
        return render(request, 'candidates/pre_pageant_edit.html', {'form': form})
