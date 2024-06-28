from django import forms

from topsis.models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'

class YearForm(forms.Form):
    year = forms.IntegerField(label='Enter Year')