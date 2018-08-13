from django.shortcuts import render
from candidates.models import *
from .forms import *
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required(login_url='admin:login')
def index(request):
    context = {

    }

    return render(request, 'candidates/index.html', context)


@login_required(login_url='admin:login')
def pre_pageant_list(request):
    data = PrePageant.objects.filter(judge=request.user).order_by('-total')
    return render(request, 'candidates/pre_pageant_list.html', {'data': data})


@login_required(login_url='admin:login')
def pre_pageant_detail(request, pk):
    data = get_object_or_404(PrePageant, pk=pk)
    return render(request, 'candidates/pre_pageant_detail.html', {'data': data})


@login_required(login_url='admin:login')
def pre_pageant_add(request):
    if request.method == "POST":
        form = PrePageantForm(request.POST)

        if PrePageant.objects.get(judge=request.user, candidate__id=request.POST['candidate']):
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
def pre_pageant_overview(request):
    pass


@login_required(login_url='admin:login')
def formal_attire_list(request):
    data = FormalAttire.objects.filter(judge=request.user).order_by('-total')
    return render(request, 'candidates/formal_attire_list.html', {'data': data})


@login_required(login_url='admin:login')
def formal_attire_detail(request, pk):
    data = get_object_or_404(FormalAttire, pk=pk)
    return render(request, 'candidates/formal_attire_detail.html', {'data': data})


@login_required(login_url='admin:login')
def formal_attire_add(request):
    if request.method == "POST":
        form = FormalAttireForm(request.POST)

        try:
            FormalAttire.objects.get(judge=request.user, candidate__id=request.POST['candidate'])
        except (FormalAttire.DoesNotExist):

            if form.is_valid():
               formal_attire = form.save(commit=False)
               formal_attire.judge = request.user
               formal_attire.total = float(
                  formal_attire.beauty_and_physique / 100.0000 * 40 +
                   formal_attire.poise_and_elegance / 100.0000 * 30 +
                    formal_attire.confidence / 100.0000 * 20 +
                    formal_attire.stage_presence / 100.0000 * 10)
            formal_attire.save()

            formal_attire_compute_total(request.POST['candidate'])

            # return redirect('formal_attire_detail', pk=formal_attire.pk)
            return redirect('formal_attire_list')

        # if object exists, render form again
        form = FormalAttireForm
        return render(request, 'candidates/formal_attire_add.html', {'form': form})
    else:
        form = FormalAttireForm
        return render(request, 'candidates/formal_attire_add.html', {'form': form})


@login_required(login_url='admin:login')
def formal_attire_edit(request, pk):
    formal_attire = get_object_or_404(FormalAttire, pk=pk)

    if request.method == "POST":
        form = FormalAttireForm(request.POST, instance=formal_attire)

        if form.is_valid():
            formal_attire = form.save(commit=False)
            formal_attire.judge = request.user
            formal_attire.total = float(
                formal_attire.beauty_and_physique / 100.0000 * 40 +
                formal_attire.poise_and_elegance / 100.0000 * 30 +
                formal_attire.confidence / 100.0000 * 20 +
                formal_attire.stage_presence / 100.0000 * 10)
            formal_attire.save()

            formal_attire_compute_total(request.POST['candidate'])

            # return redirect('formal_attire_detail', pk=formal_attire.pk)
            return redirect('candidates:formal_attire_list')
    else:
        form = FormalAttireForm(instance=formal_attire)
        return render(request, 'candidates/formal_attire_edit.html', {'form': form})


@login_required(login_url='admin:login')
def formal_attire_overview(request):
    data = FormalAttireTotal.objects.all().order_by('-total')
    return render(request, 'candidates/formal_attire_overview.html', {'data': data})


def formal_attire_compute_total(id):
    counter, beauty_and_physique, poise_and_elegance, confidence, stage_presence, total = 0, 0, 0, 0, 0, 0

    # get all votes of a candidate
    for each in FormalAttire.objects.filter(candidate__id=id):
        counter += 1

        beauty_and_physique += each.beauty_and_physique
        poise_and_elegance += each.poise_and_elegance
        confidence += each.confidence
        stage_presence += each.stage_presence
        total += each.total

    formal_attire_total = FormalAttireTotal.objects.get(candidate__id=id)
    formal_attire_total.candidate = Candidate.objects.get(id=id)
    formal_attire_total.beauty_and_physique = beauty_and_physique / counter
    formal_attire_total.poise_and_elegance = poise_and_elegance / counter
    formal_attire_total.confidence = confidence / counter
    formal_attire_total.stage_presence = stage_presence / counter
    formal_attire_total.total = total / counter
    formal_attire_total.votes = counter
    formal_attire_total.save()


@login_required(login_url='admin:login')
def formal_attire_add_all(request):
    pass


def formal_attire_add_all_logic(request):
    pass


@login_required(login_url='admin:login')
def uniform_attire_list(request):
    pass


@login_required(login_url='admin:login')
def uniform_attire_detail(request, pk):
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
def old_street_fashion_attire_detail(request, pk):
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
def question_and_answer_detail(request, pk):
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
