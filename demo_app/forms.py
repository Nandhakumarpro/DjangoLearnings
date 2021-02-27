from django import forms
from .models import ModelB, ModelC

class ModelBForm(forms.ModelForm):
    class Meta:
        model = ModelB
        fields = "__all__"

class ModelCForm(forms.ModelForm):
    class Meta:
        model = ModelC
        fields = "__all__"
