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
            return redirect('candidates:formal_attire_list')

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


def formal_attire_compute_total(idx):
    counter, beauty_and_physique, poise_and_elegance, confidence, stage_presence, total = 0, 0, 0, 0, 0, 0

    # get all votes of a candidate
    for each in FormalAttire.objects.filter(candidate__id=idx):
        counter += 1

        beauty_and_physique += each.beauty_and_physique
        poise_and_elegance += each.poise_and_elegance
        confidence += each.confidence
        stage_presence += each.stage_presence
        total += each.total

    formal_attire_total = FormalAttireTotal.objects.get(candidate__id=idx)
    formal_attire_total.candidate = Candidate.objects.get(id=idx)
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
    data = UniformAttire.objects.filter(judge=request.user).order_by('-total')
    return render(request, 'candidates/uniform_attire_list.html', {'data': data})


@login_required(login_url='admin:login')
def uniform_attire_detail(request, pk):
    data = get_object_or_404(UniformAttire, pk=pk)
    return render(request, 'candidates/uniform_attire_detail.html', {'data': data})


@login_required(login_url='admin:login')
def uniform_attire_add(request):
    if request.method == "POST":
        form = UniformAttireForm(request.POST)

        try:
            UniformAttire.objects.get(judge=request.user, candidate__id=request.POST['candidate'])
        except UniformAttire.DoesNotExist:
            if form.is_valid():
               uniform_attire = form.save(commit=False)
               uniform_attire.judge = request.user
               uniform_attire.total = float(
                    uniform_attire.poise_and_bearing / 100.0000 * 40 +
                    uniform_attire.personality / 100.0000 * 20 +
                    uniform_attire.beauty / 100.0000 * 20 +
                    uniform_attire.performance_and_confidence / 100.0000 * 20)

            uniform_attire.save()

            # re-compute total scores
            uniform_attire_compute_total(request.POST['candidate'])

            # return redirect('formal_attire_detail', pk=formal_attire.pk)
            return redirect('candidates:uniform_attire_list')

        # if object exists, render form again
        form = UniformAttireForm
        return render(request, 'candidates/uniform_attire_add.html', {'form': form})
    else:
        form = UniformAttireForm
        return render(request, 'candidates/uniform_attire_add.html', {'form': form})


@login_required(login_url='admin:login')
def uniform_attire_edit(request, pk):
    uniform_attire = get_object_or_404(UniformAttire, pk=pk)

    if request.method == "POST":
        form = UniformAttireForm(request.POST, instance=uniform_attire)

        if form.is_valid():
            uniform_attire = form.save(commit=False)
            uniform_attire.judge = request.user
            uniform_attire.total = float(
                uniform_attire.poise_and_bearing / 100.0000 * 40 +
                uniform_attire.personality / 100.0000 * 20 +
                uniform_attire.beauty / 100.0000 * 20 +
                uniform_attire.performance_and_confidence / 100.0000 * 20)
            uniform_attire.save()

            uniform_attire_compute_total(request.POST['candidate'])

            # return redirect('uniform_attire_detail', pk=uniform_attire.pk)
            return redirect('candidates:uniform_attire_list')
    else:
        form = UniformAttireForm(instance=uniform_attire)
        return render(request, 'candidates/uniform_attire_edit.html', {'form': form})


@login_required(login_url='admin:login')
def uniform_attire_overview(request):
    data = UniformAttireTotal.objects.all().order_by('-total')
    return render(request, 'candidates/uniform_attire_overview.html', {'data': data})


def uniform_attire_compute_total(idx):
    counter, poise_and_bearing, personality, beauty, performance_and_confidence, total = 0, 0, 0, 0, 0, 0

    # get all votes of a candidate
    for each in UniformAttire.objects.filter(candidate__id=idx):
        counter += 1

        poise_and_bearing += each.poise_and_bearing
        personality += each.personality
        beauty += each.beauty
        performance_and_confidence += each.performance_and_confidence
        total += each.total

    uniform_attire_total = UniformAttireTotal.objects.get(candidate__id=idx)
    uniform_attire_total.candidate = Candidate.objects.get(id=idx)
    uniform_attire_total.poise_and_bearing = poise_and_bearing / counter
    uniform_attire_total.personality = personality / counter
    uniform_attire_total.beauty = beauty / counter
    uniform_attire_total.performance_and_confidence = performance_and_confidence / counter
    uniform_attire_total.total = total / counter
    uniform_attire_total.votes = counter
    uniform_attire_total.save()


@login_required(login_url='admin:login')
def uniform_attire_add_all(request):
    pass


def uniform_attire_add_all_logic(request):
    pass


@login_required(login_url='admin:login')
def old_street_fashion_attire_list(request):
    data = OldStreetFashionAttire.objects.filter(judge=request.user).order_by('-total')
    return render(request, 'candidates/old_street_fashion_attire_list.html', {'data': data})


@login_required(login_url='admin:login')
def old_street_fashion_attire_detail(request, pk):
    data = get_object_or_404(OldStreetFashionAttire, pk=pk)
    return render(request, 'candidates/old_street_fashion_attire_detail.html', {'data': data})


@login_required(login_url='admin:login')
def old_street_fashion_attire_add(request):
    if request.method == "POST":
        form = OldStreetFashionAttireForm(request.POST)

        try:
            OldStreetFashionAttire.objects.get(judge=request.user, candidate__id=request.POST['candidate'])
        except OldStreetFashionAttire.DoesNotExist:
            if form.is_valid():
                old_street_fashion_attire = form.save(commit=False)
                old_street_fashion_attire.judge = request.user
                old_street_fashion_attire.total = float(
                    old_street_fashion_attire.poise_and_bearing / 100.0000 * 40 +
                    old_street_fashion_attire.personality / 100.0000 * 20 +
                    old_street_fashion_attire.beauty / 100.0000 * 20 +
                    old_street_fashion_attire.performance_and_confidence / 100.0000 * 20)

            old_street_fashion_attire.save()

            # re-compute total scores
            old_street_fashion_attire_compute_total(request.POST['candidate'])

            # return redirect('formal_attire_detail', pk=formal_attire.pk)
            return redirect('candidates:old_street_fashion_attire_list')

        # if object exists, render form again
        form = OldStreetFashionAttireForm
        return render(request, 'candidates/old_street_fashion_attire_add.html', {'form': form})
    else:
        form = OldStreetFashionAttireForm
        return render(request, 'candidates/old_street_fashion_attire_add.html', {'form': form})


@login_required(login_url='admin:login')
def old_street_fashion_attire_edit(request, pk):
    old_street_fashion_attire = get_object_or_404(OldStreetFashionAttire, pk=pk)

    if request.method == "POST":
        form = OldStreetFashionAttireForm(request.POST, instance=old_street_fashion_attire)

        if form.is_valid():
            old_street_fashion_attire = form.save(commit=False)
            old_street_fashion_attire.judge = request.user
            old_street_fashion_attire.total = float(
                old_street_fashion_attire.poise_and_bearing / 100.0000 * 40 +
                old_street_fashion_attire.personality / 100.0000 * 20 +
                old_street_fashion_attire.beauty / 100.0000 * 20 +
                old_street_fashion_attire.performance_and_confidence / 100.0000 * 20)
            old_street_fashion_attire.save()

            old_street_fashion_attire_compute_total(request.POST['candidate'])

            # return redirect('old_street_fashion_attire_detail', pk=old_street_fashion_attire.pk)
            return redirect('candidates:old_street_fashion_attire_list')
    else:
        form = OldStreetFashionAttireForm(instance=old_street_fashion_attire)
        return render(request, 'candidates/old_street_fashion_attire_edit.html', {'form': form})


@login_required(login_url='admin:login')
def old_street_fashion_attire_overview(request):
    data = OldStreetFashionAttireTotal.objects.all().order_by('-total')
    return render(request, 'candidates/old_street_fashion_attire_overview.html', {'data': data})


def old_street_fashion_attire_compute_total(idx):
    counter, poise_and_bearing, personality, beauty, performance_and_confidence, total = 0, 0, 0, 0, 0, 0

    # get all votes of a candidate
    for each in OldStreetFashionAttire.objects.filter(candidate__id=idx):
        counter += 1

        poise_and_bearing += each.poise_and_bearing
        personality += each.personality
        beauty += each.beauty
        performance_and_confidence += each.performance_and_confidence
        total += each.total

    old_street_fashion_attire_total = OldStreetFashionAttireTotal.objects.get(candidate__id=idx)
    old_street_fashion_attire_total.candidate = Candidate.objects.get(id=idx)
    old_street_fashion_attire_total.poise_and_bearing = poise_and_bearing / counter
    old_street_fashion_attire_total.personality = personality / counter
    old_street_fashion_attire_total.beauty = beauty / counter
    old_street_fashion_attire_total.performance_and_confidence = performance_and_confidence / counter
    old_street_fashion_attire_total.total = total / counter
    old_street_fashion_attire_total.votes = counter
    old_street_fashion_attire_total.save()


@login_required(login_url='admin:login')
def old_street_fashion_attire_add_all(request):
    pass


def old_street_fashion_attire_add_all_logic(request):
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
