from django import forms
from .models import ( ModelB, ModelC, ModelB1, ModelB2,
    ModelC1, ModelC2, ModelD, ModelA,Product)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

class ModelBForm(forms.Form):
    variableB1 = forms.ModelChoiceField( queryset= ModelB1.objects.all() , required= True)
    variableB2 = forms.IntegerField(required =True )
    variableB3 = forms.ModelChoiceField(  queryset= ModelB2.objects.all() , required= True)
    variableB4 = forms.ModelChoiceField(  queryset = ModelB1.objects.all() , required= True)
    variableB5 = forms.IntegerField(required =True )
    class Meta:
        fields = "__all__"

class ModelCForm(forms.Form):
    variableC1 = forms.ModelChoiceField( queryset= ModelC1.objects.all() , required= True)
    variableC2 = forms.IntegerField(required =True ,max_value=1000)
    variableC3 = forms.ModelChoiceField( queryset = ModelC2.objects.all() , required= True)
    variableC4 = forms.ModelChoiceField(queryset= ModelC1.objects.all() , required= True)
    variableC5 = forms.IntegerField(required =True )

class DateInput(forms.DateInput):
    input_type = 'date'

class ModelAForm(forms.Form):
    buy_sell = forms.ChoiceField( choices=(("buy", "Buy"), ("sell", "Sell") ),required =True )
    variableA1 = forms.ModelMultipleChoiceField(queryset = ModelD.objects.all(), required = True )
    date_start = forms.DateField(required = True,widget=forms.SelectDateWidget(years=range(2000,2021)) )
    date_end = forms.DateField(required = True,widget=forms.SelectDateWidget(years=range(2000,2021)))
    variableA2 = forms.ChoiceField(choices = ( ("aa1", "AA1"), ("aa2", "AA2")),required = True )

    class Meta:
        model = ModelA
        fields = "__all__"
        widgets = {
            "date_start": DateInput(),
            "date_end": DateInput()
        }
