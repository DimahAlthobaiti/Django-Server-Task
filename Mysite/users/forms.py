from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']

        age = forms.IntegerField(min_value=0, label='Age')