from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Candidate(models.Model):
    idx = models.IntegerField(null=True)
    picture = models.ImageField(default="default.png")
    first_name = models.CharField(max_length=50)
    middle_initial = models.CharField(blank=True, max_length=5)
    last_name = models.CharField(max_length=50)
    program = models.CharField(max_length=50)
    sex = models.CharField(max_length=8, choices=(('Male', 'Male'), ('Female', 'Female')))
    age = models.IntegerField(blank=True)
    order = models.IntegerField(null=True)


# Individual instances
class PrePageant(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    corporate_attire = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    panel_interview = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    essay = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    talent = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(null=True)


class OldStreetFashionAttire(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    poise_and_bearing = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    personality = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    beauty = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    performance_and_confidence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(null=True)


class UniformAttire(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    poise_and_bearing = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    personality = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    beauty = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    performance_and_confidence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(null=True)


class FormalAttire(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    beauty_and_physique = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    poise_and_elegance = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    confidence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    stage_presence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(null=True)


class QuestionAndAnswer(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    judge = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])


# Totals
class PrePageantTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    corporate_attire = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    panel_interview = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    essay = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    talent = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(null=True)


class OldStreetFashionAttireTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    poise_and_bearing = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    personality = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    beauty = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    performance_and_confidence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(null=True)


class UniformAttireTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    poise_and_bearing = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    personality = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    beauty = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    performance_and_confidence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(null=True)


class FormalAttireTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    beauty_and_physique = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    poise_and_elegance = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    confidence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    stage_presence = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(null=True)


class QuestionAndAnswerTotal(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    total = models.FloatField(null=True)


class PageantProper(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    old_street_fashion = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    uniform = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    formal_attire = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])


class PageantNight(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    pre_pageant = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    pageant_proper = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    total = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])


class PageantResult(models.Model):
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    pageant_night = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    question_and_answer = models.FloatField(validators=[MaxValueValidator(100), MinValueValidator(0)])


