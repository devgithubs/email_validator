from django import forms
from .models import Word, EmailTest


class TextForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = '__all__'
        labels = {
            'text': 'Email Address'
        }
        

class EmailTestForm(forms.ModelForm):
    class Meta:
        model = EmailTest
        fields = ('email', 'test_conditions')
        widgets = {
            'test_conditions': forms.CheckboxSelectMultiple(),
        }
