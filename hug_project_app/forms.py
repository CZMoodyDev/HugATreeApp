from django import forms
from hug_project_app.models import Photo

class PhotoForm(forms.Form):
    picture = forms.ImageField()




