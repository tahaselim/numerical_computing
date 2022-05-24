
## python code to calculate the integral based
# on trapezoidal rule for npoint+1 even-spaced 
# grid of points
#### T. Selim 
#### www.tiselim.com

## The code is used to approximate the integral:
# ∫_a^b f(x) dx =   
# (b - a)/(2*npoint) sum_{i=1}^n ( f(x_{i} + f_{x+i}) ) 

# import numpy
import numpy as np

def trapz_int1(f,a,b,npoint):
## variables
#     a:      the lower bound of the integral
#     b:      the upper bound of the integral 
#     npoint: the number of points whose is used to approximate 
#     the integral 
# Returns
#     -------
#     float
#         Approximation of the integral of f(x) from a to b using the
#         trapezoid rule with N subintervals of equal length.

    y_list = []
    points = np.linspace(a,b,npoint+1)
    x = points
    for i in range(0,npoint+1):
        y_list.append(f(x[i]))
    # y = f(x) # the function
    I= 0
    delta = (b-a)/(2*npoint)
    for i in range(0,npoint):
        I += (y_list[i] + y_list[i+1])*delta
    return  I
