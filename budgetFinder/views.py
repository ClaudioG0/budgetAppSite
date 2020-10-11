from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import *
import time

def overSpending(request):
    return render(request, 'budgetFinder/overspending.html')

def shopping(request):
    return render(request, "budgetFinder/shopping.html")

def index(request):
    formRev = RevForm(request.POST or None)
    formExp = ExpForm(request.POST or None)
    dataTest = 0
    totRev = 0
    totExp = 0
    page = ""
    if formRev.is_valid() and 'submit' in request.POST:
        totRev = formRev.cleaned_data.get("saving") +\
                 formRev.cleaned_data.get("salary") +\
                 formRev.cleaned_data.get("investment") +\
                 formRev.cleaned_data.get("other_income")
    if formExp.is_valid() and 'submit' in request.POST:
        totExp = formExp.cleaned_data.get('rent') +\
                 formExp.cleaned_data.get('food') +\
                 formExp.cleaned_data.get('entertainment') +\
                 formExp.cleaned_data.get('other_expenses')
    result = totRev - totExp
    if result <= 0 and 'submit' in request.POST:

        return redirect('overspending/')
    elif result > 0:

        return redirect('shopping/')
    context = {

    "formRev": formRev,
    "formExp": formExp,
    "page": page,
    "dataTest": dataTest,
    "result": result,
    }
    result = None

    return render(request, 'budgetFinder/index.html', context)

