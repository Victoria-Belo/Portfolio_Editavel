from django import forms
from app.models import Note
from django.forms import ModelForm


class noteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = ['create_at', 'update_at']

    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": '', "class": 'form-control'}))
    sub_title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": '', "class": 'form-control'}))
    note = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": '', "class": 'form-control'}))
    notice = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": '', "class": 'form-control'}))
