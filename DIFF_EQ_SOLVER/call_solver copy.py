from sympy import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from DiffEqSolver import SolveOde

"""INITIATE THE SYMBOLS, FUNCTIONS, AND PRETTY PRINTING"""

x,y,z = symbols('x,y,z', positive = True)
init_printing(use_latex=True)
f,g = symbols('f,g', cls = Function, positive = True)

"""
    CREATE AN EXQUATION AND CONDITION LIKE THE FOLLOWING

    equation = Eq(f(x).diff(x,x,x) + f(x).diff(x),exp(x))
    conditions_dict = {f(0) :0,f(x).diff(x).subs(x,0):0, f(x).diff(x,x).subs(x,0):0}
"""

equation = Eq(f(x).diff(x,x,x) + f(x).diff(x),exp(x))
conditions_dict = {f(0) :0,f(x).diff(x).subs(x,0):0, f(x).diff(x,x).subs(x,0):0}

solve_ode = SolveOde(equation, conditions_dict)
solve_ode.compute_ode()
