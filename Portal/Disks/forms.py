from django import forms
from .models import Disk


class DiskForm(forms.ModelForm):
    class Meta:
        model = Disk
        fields = ['genre', 'title']
