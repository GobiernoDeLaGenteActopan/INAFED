from django import forms
from .models import Indicador


class UploadFileForm(forms.ModelForm):
    evidencia = forms.FileField(label="")
    class Meta:
        model = Indicador
        fields = ['evidencia']