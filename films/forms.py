from django import forms
from .models import film


class filmForm(forms.ModelForm):
    class Meta:
        model = film
        fields = ["title", "content", "image"]
        