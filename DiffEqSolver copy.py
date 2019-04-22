from sympy import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x,y,z = symbols('x,y,z', positive = True)
init_printing(use_latex=True)
f,g = symbols('f,g', cls = Function, positive = True)


class SolveOde:

    def __init__(self, equation, conditions_dict):
        self.equation = equation
        self.conditions_dict = conditions_dict


    def compute_ode(self):
        ode = dsolve(self.equation, ics = self.conditions_dict)

        function = lambdify(x,ode.rhs,'numpy')
        print(ode)

        return function
    def plot(self, x_lower, x_upper, step = .01):
        f_ = self.compute_ode()

        plot_dict = {}
        for i in np.arange(x_lower, x_upper,step):
            y = f_(i)
            plot_dict[i] = y

        plt.plot(plot_dict.keys(), plot_dict.values())
        plt.show()
