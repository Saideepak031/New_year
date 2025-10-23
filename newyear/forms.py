from django import forms
from .models import Note, Goal, Wish

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Note title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Important points...','rows':4}),
        }

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['text']
        widgets = {'text': forms.TextInput(attrs={'placeholder': 'Add a new goal...'})}

class WishForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['text']
        widgets = {'text': forms.TextInput(attrs={'placeholder': 'Write a wish...'})}