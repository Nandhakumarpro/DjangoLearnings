from django.shortcuts import render, reverse
from django import views
from django.http import HttpResponseRedirect
from .models import  ModelB, ModelC, Product
from .serializers import  ModelASerializer

import requests

from .forms import ModelBForm, ModelCForm, ModelAForm, ProductForm
# Create your views here.
'model_a-detail'
BASE = 'http://127.0.0.1:8000'

def delete_orphaned_records():
    [ i.delete() for i in ModelB.objects.filter(product=None).all() ]
    [ i.delete() for i in ModelC.objects.filter(product=None).all() ]

def set_product_for_orphaned_records(product):
    for i in ModelB.objects.filter(product=None).all():
        i.product = product
        i.save()
    for i in ModelC.objects.filter(product=None).all():
        i.product = product
        i.save()

def create_product(request):
    prod_form = ProductForm(auto_id="prod_form_%s")
    a_form = ModelAForm(auto_id="aform_%s")
    b_form = ModelBForm(auto_id="bform_%s")
    c_form = ModelCForm(auto_id="cform_%s")
    context = dict(b_form = b_form, c_form = c_form, a_form=a_form,prod_form=prod_form)
    if request.method == "POST":
        prod_form = ProductForm(request.POST)
        a_form = ModelAForm(request.POST)
        if a_form.is_valid() and prod_form.is_valid() :#and b_form.is_valid() and c_form.is_valid():
            product = prod_form.save()
            for var_a1 in a_form.cleaned_data.pop('variableA1'):
                data = {**a_form.cleaned_data,'variableA1': var_a1.pk,"product":product.pk}
                serializer = ModelASerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                else:
                    print(serializer.errors)

            set_product_for_orphaned_records(product)
    delete_orphaned_records()
    return render(request, "product-create.html", context=context)

def list_product(request):
    products = Product.objects.all()
    return render(request, "product-list.html", context = {"products":products})

def detail_product(request, pk):
    pass
