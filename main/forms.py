from django import forms
from .models import Animal

class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    check = forms.BooleanField(required=False)

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'isfavourite']