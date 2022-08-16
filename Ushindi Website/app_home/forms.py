from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm 
from .models import *

class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = '__all__'

class SongForm(forms.ModelForm):
    class Meta:
        model = SongPost

        fields = ('title', 'body', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Testimony'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Testimony'}),
            # 'body': forms.ImageField(attrs={'class': 'form-control', 'placeholder': 'image'})
        }