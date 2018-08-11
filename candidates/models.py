from django.db import models
from django.contrib.auth.models import User


class Candidate(models.Model):
    id = models.IntegerField(primary_key=True)
    picture = models.ImageField(default="default.png")
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(blank=True, max_length=5)
    last_name = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    sex = models.BooleanField()
    age = models.IntegerField(blank=True)
    order = models.IntegerField(null=True)


# Individual instances
class PrePageant(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    corporate_attire = models.FloatField()
    panel_interview = models.FloatField()
    essay = models.FloatField()
    talent = models.FloatField()
    total = models.FloatField(null=True)


class OldStreetFashionAttire(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    poise_and_bearing = models.FloatField()
    personality = models.FloatField()
    beauty = models.FloatField()
    performance_and_confidence = models.FloatField()
    total = models.FloatField(null=True)


class UniformAttire(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    poise_and_bearing = models.FloatField()
    personality = models.FloatField()
    beauty = models.FloatField()
    performance_and_confidence = models.FloatField()
    total = models.FloatField(null=True)


class FormalAttire(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    beauty_and_physique = models.FloatField()
    poise_and_elegance = models.FloatField()
    confidence = models.FloatField()
    stage_presence = models.FloatField()
    total = models.FloatField(null=True)


class QuestionAndAnswer(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()


# Totals
class PrePageantTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    corporate_attire = models.FloatField()
    panel_interview = models.FloatField()
    essay = models.FloatField()
    talent = models.FloatField()
    total = models.FloatField(null=True)


class OldStreetFashionAttireTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    poise_and_bearing = models.FloatField()
    personality = models.FloatField()
    beauty = models.FloatField()
    performance_and_confidence = models.FloatField()
    total = models.FloatField(null=True)


class UniformAttireTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    poise_and_bearing = models.FloatField()
    personality = models.FloatField()
    beauty = models.FloatField()
    performance_and_confidence = models.FloatField()
    total = models.FloatField(null=True)


class FormalAttireTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    beauty_and_physique = models.FloatField()
    poise_and_elegance = models.FloatField()
    confidence = models.FloatField()
    stage_presence = models.FloatField()
    total = models.FloatField(null=True)


class QuestionAndAnswerTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    total = models.FloatField(null=True)


class PageantProper(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    old_street_fashion = models.FloatField()
    uniform = models.FloatField()
    formal_attire = models.FloatField()
    total = models.FloatField()


class PageantNight(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    pre_pageant = models.FloatField()
    pageant_proper = models.FloatField()
    total = models.FloatField()


class PageantResult(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    pageant_night = models.FloatField()
    question_and_answer = models.FloatField()


