from django import forms
from .models import Note

class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['name', 'email']
    name = forms.CharField(
        max_length=512,
        widget=forms.TextInput
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput
    )
