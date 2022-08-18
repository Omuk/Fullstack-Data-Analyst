from xml.etree.ElementInclude import include
from .models import *
from django import forms
from django.forms import ModelForm

class AlbumForm(forms.ModelForm):
    class Meta:
        model = GalleryPoster
        fields = '__all__'

    zip = forms.FileField(required=False)

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pictures'] = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
    class Meta:
        model = NewAlbums
        fields = '__all__'

# class NewPostForm(forms.ModelForm):
#     title = forms.CharField(max_length=128)
#     content = forms.CharField(max_length=245, label="Item Description.")

#     class Meta:
#         model = GalleryPoster
#         fields = ('title', 'content', )


# class ImageForm(forms.ModelForm):
#     image = forms.ImageField(label='Image')    
#     class Meta:
#         model = Images
#         fields = ('image', )

# class GalForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['pictures'] = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    
#     class Meta:
#         model = GalleryPoster
#         fields = '__all__'