from django import forms

class uploadImage(forms.Form):
    img = forms.ImageField(required=True,label="image_uploaded")