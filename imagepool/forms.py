from django import forms

class ImageUploadForm(forms.Form):
    file_to_upload = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple':True}))
