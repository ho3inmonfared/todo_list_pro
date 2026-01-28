from django import forms 

from . import models

class TaskForm(forms.ModelForm):
    class Meta:
        model=models.Task
        fields=['text','category']
        widgets = {
            'text': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:border-indigo-400',
                'placeholder': 'کار جدید اضافه کنید...'
            }),
            'category': forms.Select(attrs={
                'class': 'px-3 py-2 rounded-lg border border-gray-200'
            })
            }
