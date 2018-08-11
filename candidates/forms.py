from django import forms

from .models import PrePageant

class PrePageantForm(forms.ModelForm):
    class Meta:
        model = PrePageant
        fields = ('candidate', 'corporate_attire', 'panel_interview', 'essay', 'talent')