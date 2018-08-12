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


@login_required(login_url='admin:login')
def formal_attire_list(request):
    pass


@login_required(login_url='admin:login')
def formal_attire_details(request, pk):
    pass


@login_required(login_url='admin:login')
def formal_attire_add(request):
    pass


@login_required(login_url='admin:login')
def formal_attire_edit(request, pk):
    pass


@login_required(login_url='admin:login')
def formal_attire_add_all(request):
    pass


@login_required(login_url='admin:login')
def formal_attire_overview(request):
    pass


def formal_attire_add_all_logic(request):
    pass


def formal_attire_compute_total():
    pass


@login_required(login_url='admin:login')
def uniform_attire_list(request):
    pass


@login_required(login_url='admin:login')
def uniform_attire_details(request, pk):
    pass


@login_required(login_url='admin:login')
def uniform_attire_add(request):
    pass


@login_required(login_url='admin:login')
def uniform_attire_edit(request, pk):
    pass


@login_required(login_url='admin:login')
def uniform_attire_add_all(request):
    pass


@login_required(login_url='admin:login')
def uniform_attire_overview(request):
    pass


def uniform_attire_add_all_logic(request):
    pass


def uniform_attire_compute_total():
    pass


@login_required(login_url='admin:login')
def old_street_fashion_attire_list(request):
    pass


@login_required(login_url='admin:login')
def old_street_fashion_attire_details(request, pk):
    pass


@login_required(login_url='admin:login')
def old_street_fashion_attire_add(request):
    pass


@login_required(login_url='admin:login')
def old_street_fashion_attire_edit(request, pk):
    pass


@login_required(login_url='admin:login')
def old_street_fashion_attire_add_all(request):
    pass


@login_required(login_url='admin:login')
def old_street_fashion_attire_overview(request):
    pass


def old_street_fashion_attire_add_all_logic(request):
    pass


def old_street_fashion_attire_compute_total():
    pass


@login_required(login_url='admin:login')
def question_and_answer_list(request):
    pass


@login_required(login_url='admin:login')
def question_and_answer_details(request, pk):
    pass


@login_required(login_url='admin:login')
def question_and_answer_add(request):
    pass


@login_required(login_url='admin:login')
def question_and_answer_edit(request, pk):
    pass


@login_required(login_url='admin:login')
def question_and_answer_add_all(request):
    pass


@login_required(login_url='admin:login')
def question_and_answer_overview(request):
    pass


def question_and_answer_add_all_logic(request):
    pass


def question_and_answer_compute_total():
    pass