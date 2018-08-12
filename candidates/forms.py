from django import forms

from .models import PrePageant, FormalAttire, QuestionAndAnswer, UniformAttire, OldStreetFashionAttire


class PrePageantForm(forms.ModelForm):
    class Meta:
        model = PrePageant
        fields = ('candidate', 'corporate_attire', 'panel_interview', 'essay', 'talent')


class FormalAttireForm(forms.ModelForm):
    class Meta:
        model = FormalAttire
        fields = ('candidate', 'beauty_and_physique', 'poise_and_elegance', 'confidence', 'stage_presence')


class UniformAttireForm(forms.ModelForm):
    class Meta:
        model = UniformAttire
        fields = ('candidate', 'poise_and_bearing', 'personality', 'beauty', 'performance_and_confidence')


class OldStreetFashionAttireForm(forms.ModelForm):
    class Meta:
        model = OldStreetFashionAttire
        fields = ('candidate', 'poise_and_bearing', 'personality', 'beauty', 'performance_and_confidence')


class QuestionAndAnswerForm(forms.ModelForm):
    class Meta:
        model = QuestionAndAnswer
        fields = ('candidate', 'total')