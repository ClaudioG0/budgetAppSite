from django import forms
from django.forms import ModelForm
from .models import *

class RevForm(forms.ModelForm):
    saving = forms.IntegerField(widget = forms.NumberInput
    (attrs={'placeholder': "Enter total", 'name': "savings", 'id': "savings", 'type': "number", 'min': 0}))

    salary = forms.IntegerField(widget = forms.NumberInput
    (attrs={'placeholder': "Enter yearly income", 'name': "salary", 'id': "salary", 'type': "number", 'min': 0}))

    investment = forms.IntegerField(widget = forms.NumberInput
    (attrs={'placeholder': "Enter monthly income", 'name': "investment", 'id': "investment", 'type': "number", 'min': 0}))

    other_income = forms.IntegerField(widget = forms.NumberInput
    (attrs={'placeholder': "Enter monthly amount", 'name': "other_income", 'id': "other_income", 'type': "number", 'min': 0}))

    class Meta:
        model = Task
        fields = '__all__'


class ExpForm(forms.ModelForm):
    rent = forms.IntegerField(widget=forms.NumberInput
    (attrs={'placeholder': "Enter monthly amount", 'name': "rent", 'id': "rent", 'type': "number", 'min': 0}))

    food = forms.IntegerField(widget=forms.NumberInput
    (attrs={'placeholder': "Enter monthly amount", 'name': "Food", 'id': "Food", 'type': "number", 'min': 0}))

    entertainment = forms.IntegerField(widget=forms.NumberInput
    (attrs={'placeholder': "Enter monthly amount", 'name': "entertaintment", 'id': "entertaintment", 'type': "number", 'min': 0}))

    other_expenses = forms.IntegerField(widget = forms.NumberInput
    (attrs={'placeholder': "Enter monthly amount", 'name': "other_expenses", 'id': "other_expenses", 'type': "number", 'min': 0}))


    class Meta:
        model = Task
        fields = '__all__'