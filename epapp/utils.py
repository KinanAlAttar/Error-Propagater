from sympy import *

def evaluate_partial(partial, values):
  for key, val in values.items():
    partial = partial.subs(key, val[0])

  return partial

def get_error(equation, values):
  err = 0

  for key, val in values.items():
    var = Symbol(key)
    partial = diff(equation, var)
    evaluated_partial = evaluate_partial(partial, values)
    err += (evaluated_partial*val[1])**2

  return err**(1/2)

def get_val(equation, values):
  for key, val in values.items():
    equation = equation.subs(key, val[0])

  return equation