from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from epapp.utils import get_error, get_val
from sympy.core import sympify

def index(request):
  return render(request, 'epapp/index.html')

def submit(request):
  form = request.POST
  eq   = sympify(form['eq'])
  syms = form.getlist('var-sym')
  vals = form.getlist('var-val')
  uncs = form.getlist('var-unc')

  values = {}

  for var, val, unc in zip(syms, vals, uncs):
    values[var] = (float(val), float(unc))

  result = (get_error(eq, values), get_val(eq, values))

  return render(request, 'epapp/index.html', {'results': result})