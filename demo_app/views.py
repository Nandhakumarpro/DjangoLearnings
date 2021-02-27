from django.shortcuts import render, reverse
from django import views
from django.http import HttpResponseRedirect

import requests

from .forms import ModelBForm, ModelCForm
# Create your views here.

BASE = 'http://127.0.0.1:8000'

def index(request):
    b_form = ModelBForm()
    c_form = ModelCForm(auto_id="test_%s")
    model_b_set = requests.get(BASE + reverse("model_b-list")).json()
    model_c_set = requests.get(BASE + reverse("model_c-list")).json()
    context = dict(b_form = b_form, c_form = c_form, model_b_set = model_b_set, model_c_set = model_c_set)
    return render(request, "ajax.html", context=context)
