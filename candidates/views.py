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

        try:
            PrePageant.objects.get(judge=request.user, candidate__id=request.POST['candidate'])
        except:
            if form.is_valid():
                prepageant = form.save(commit=False)
                prepageant.judge = request.user
                prepageant.total = float(
                    prepageant.talent / 100.0000 * 30 +
                    prepageant.essay / 100.0000 * 30 +
                    prepageant.corporate_attire / 100.0000 * 20 +
                    prepageant.panel_interview / 100.0000 * 20)
                prepageant.save()

                pre_pageant_compute_total(prepageant.pk)
            return redirect('candidates:pre_pageant_detail', pk=prepageant.pk)

        form = PrePageantForm
        return render(request, 'candidates/pre_pageant_add.html', {'form': form})
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
            return redirect('candidates:pre_pageant_detail', pk=prepageant.pk)
    else:
        form = PrePageantForm(instance=prepageant)
        return render(request, 'candidates/pre_pageant_edit.html', {'form': form})


@login_required(login_url='admin:login')
def pre_pageant_overview(request):
    data = PrePageantTotal.objects.all().order_by('-total')
    return render(request, 'candidates/pre_pageant_overview.html', {'data': data})


def pre_pageant_compute_total(idx):
    counter, corporate_attire, panel_interview, essay, talent, total = 0, 0, 0, 0, 0, 0

    # get all votes of a candidate
    for each in PrePageant.objects.filter(candidate__id=idx):
        counter += 1

        corporate_attire += each.corporate_attire
        panel_interview += each.panel_interview
        essay += each.essay
        talent += each.talent
        total += each.total

    pre_pageant_total = PrePageantTotal.objects.get(candidate__id=idx)
    pre_pageant_total.candidate = Candidate.objects.get(id=idx)
    pre_pageant_total.corporate_attire = corporate_attire / counter
    pre_pageant_total.panel_interview = panel_interview / counter
    pre_pageant_total.essay = essay / counter
    pre_pageant_total.talent = talent / counter
    pre_pageant_total.total = total / counter
    pre_pageant_total.votes = counter
    pre_pageant_total.save()


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

    pageant_proper_compute_total(idx)


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

    pageant_proper_compute_total(idx)


@login_required(login_url='admin:login')
def old_street_fashion_attire_add_all(request):
    pass


def old_street_fashion_attire_add_all_logic(request):
    pass


@login_required(login_url='admin:login')
def question_and_answer_list(request):
    data = QuestionAndAnswer.objects.filter(judge=request.user).order_by('-total')
    return render(request, 'candidates/question_and_answer_list.html', {'data': data})


@login_required(login_url='admin:login')
def question_and_answer_detail(request, pk):
    data = get_object_or_404(QuestionAndAnswer, pk=pk)
    return render(request, 'candidates/question_and_answer_detail.html', {'data': data})


@login_required(login_url='admin:login')
def question_and_answer_add(request):
    if request.method == "POST":
        form = QuestionAndAnswerForm(request.POST)

        try:
            QuestionAndAnswer.objects.get(judge=request.user, candidate__id=request.POST['candidate'])
        except QuestionAndAnswer.DoesNotExist:
            if form.is_valid():
                question_and_answer = form.save(commit=False)
                question_and_answer.judge = request.user
                question_and_answer.save()

            question_and_answer_compute_total(request.POST['candidate'])

            return redirect('candidates:question_and_answer_list')

        form = QuestionAndAnswerForm
        return render(request, 'candidates/question_and_answer_add.html', {'form': form})
    else:
        form = QuestionAndAnswerForm
        return render(request, 'candidates/question_and_answer_add.html', {'form': form})


@login_required(login_url='admin:login')
def question_and_answer_edit(request, pk):
    question_and_answer = get_object_or_404(QuestionAndAnswer, pk=pk)

    if request.method == "POST":
        form = QuestionAndAnswerForm(request.POST, instance=question_and_answer)

        if form.is_valid():
            question_and_answer = form.save(commit=False)
            question_and_answer.judge = request.user
            question_and_answer.save()

            question_and_answer_compute_total(request.POST['candidate'])

            return redirect('candidates:question_and_answer_list')
    else:
        form = QuestionAndAnswerForm(instance=question_and_answer)
        return render(request, 'candidates/question_and_answwer_edit.html', {'form': form})


@login_required(login_url='admin:login')
def question_and_answer_overview(request):
    judges = 2
    incomplete = 0
    for each in PageantNight.objects.all():
        if each.old_street_fashion_votes != judges or each.uniform_votes != judges or each.formal_attire_votes != judges:
            incomplete += 1

    if incomplete == 0:
        try:
            PageantResult.objects.all()
        except PageantResult.DoesNotExist:
            create_pageant_result()

        data = QuestionAndAnswerTotal.objects.all().sort_by('-total')
        return render(request, 'candidates/question_and_answer_overview.html', {'data': data})
    else:
        data = incomplete
        return render(request, 'candidates/question_and_answer_incomplete.html', {'data': data})


def question_and_answer_compute_total(idx):
    counter, total = 0, 0

    for each in QuestionAndAnswerTotal.objects.filter(candidate__candidate__id=idx):
        counter += 1

        total += each.total

    question_and_answer_total = QuestionAndAnswerTotal.objects.get(candidate__candidate__id=idx)
    question_and_answer_total.candidate = RankSix.object.get(id=idx)
    question_and_answer_total.total = total / counter
    question_and_answer_total.votes = counter
    question_and_answer_total.save()

    pageant_result_compute_total(idx)


def question_and_answer_add_all_logic(request):
    pass


@login_required(login_url='admin:login')
def question_and_answer_add_all(request):
    pass


def pageant_proper_compute_total(idx):
    old_street_fashion = OldStreetFashionAttireTotal.objects.filter(candidate__id=idx)
    uniform = UniformAttireTotal.objects.filter(candidate__id=idx)
    formal_attire = FormalAttireTotal.objects.filter(candidate__id=idx)

    pageant_proper = PageantProper.objects.get(candidate__id=idx)
    pageant_proper.old_street_fashion = old_street_fashion.total
    pageant_proper.uniform = uniform.total
    pageant_proper.formal_attire = formal_attire.total
    pageant_proper.old_street_fashion_votes = old_street_fashion.votes
    pageant_proper.uniform_votes = uniform.votes
    pageant_proper.formal_attire_votes = formal_attire.votes
    pageant_proper.total = (formal_attire.total / 100.0000 * 40) + (uniform.total / 100.0000 * 30) + (
                old_street_fashion.total / 100.0000 * 30)
    pageant_proper.save()

    pageant_night_compute_total(idx)


def pageant_night_compute_total(idx):
    pre_pageant = PrePageantTotal.objects.get(candidate__id=idx)
    pageant_proper = PageantProper.objects.get(candidate__id=idx)

    pageant_night = PageantNight.objects.get(candidate__id=idx)
    pageant_night.pre_pageant = pre_pageant.total
    pageant_night.pageant_proper = pageant_proper.total
    pageant_night.old_street_fashion_votes = pageant_proper.old_street_fashion_votes
    pageant_night.uniform_votes = pageant_proper.uniform_votes
    pageant_night.formal_attire_votes = pageant_proper.formal_attire_votes
    pageant_night.total = (pre_pageant.total / 100.0000 * 40) + (pageant_proper.total / 100.0000 * 60)
    pageant_night.save()

    compute_rank_six()


def compute_rank_six():
    f_counter, m_counter = 0
    RankSix.objects.all().delete()

    for x in PageantNight.objects.all().order_by('-total'):
        if x.candidate.sex == 'Female':
            if f_counter < 6:
                ranker = RankSix(candidate=x.candidate.id)
                ranker.save()
                f_counter += 1
        if x.candidate.sex == 'Male':
            if m_counter < 6:
                ranker = RankSix(candidate=x.candidate.id)
                ranker.save()
                m_counter += 1


@login_required(login_url='admin:login')
def pageant_proper_overview(request):
    data = PageantProper.objects.all()
    return render(request, 'candidates/pageant_proper_overview.html', {'data': data})


@login_required(login_url='admin:login')
def pageant_night_overview(request):
    data = PageantNight.objects.all()
    return render(request, 'candidates/pageant_night_overview.html', {'data': data})


@login_required(login_url='admin:login')
def top_candidates(request):
    data = RankSix.objects.all()
    return render(request, 'candidates/top_candidates.html', {'data': data})


def pageant_result_compute_total(idx):
    pageant_result_object = PageantResult.objects.get(candidate__id=idx)
    pn = PageantNight.objects.get(idx)
    qa = QuestionAndAnswerTotal.objects.get(idx)
    pageant_result_object.votes = qa.votes
    pageant_result_object.pageant_night = pn.total
    pageant_result_object.question_and_answer = qa.total
    pageant_result_object.total = (pn.total / 100.0000 * 40) + (qa.total / 100.0000 * 60)
    pageant_result_object.save()


def create_pageant_result():
    for each in RankSix.objects.all().order_by('-total'):
        candidate = each.candidate

        pr = PageantResult(candidate=candidate, pageant_night=0, question_and_answer=0, total=0, votes=0)
        pr.save()


@login_required(login_url='admin:login')
def pageant_result_overview(request):
    data = PageantResult.objects.all().order_by('-total')
    return render(request, 'candidates/pageant_result_overview.html', {'data': data})