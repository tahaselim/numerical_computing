import numpy as np 
import matplotlib.pyplot as plt
import sys 

# sin(x)
xx = np.arange(0,2*np.pi,0.1)
yy = np.sin(xx)

plt.plot(xx,yy)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.style.use("ggplot")
plt.show()

def trapz_int1(f,a,b,npoint):
# variables
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
    # eval the function
    for i in range(0,npoint+1):
        y_list.append(f(points[i]))
    
    I = 0
    delta = (b - a)/ npoint
    # the sum in the formula
    for i in range(0,npoint):
        I += (y_list[i] + y_list[i+1]) * delta/2
    
    return I


# we will take sin(x) as a test function 

# interval from 0 to 2pi

def fsin(x):
    y = np.sin(x)
    return y

# testing the implementation 
N = 10
a = 0
b = 2*np.pi
xx = np.linspace(a,b,N)
yy = fsin(xx)
Int_value = trapz_int1(fsin,a,b,N)
Igsin = 0
print("For N = ",N, "points", "Numerical integration is ",
Int_value)

# perform this int. over interval from 0 to pi
N = 5
a = 0
b = np.pi
xx = np.linspace(a,b,N)
yy = fsin(xx)
Int_value = trapz_int1(fsin,a,b,N)
Igsinx = 2
print("For N = ",N, "points", "Numerical integration is ",
Int_value,"the exact value is",Igsinx)

# now let's examine the convergence of the data
Nvec = []
Nvec = [2,4,6,10,12,16,20,30,40,50,60,80,100,200,500,800,1000,10000]
nNvec = len(Nvec)
Ig0  =  Igsinx 
I_list = []
err = []
for i in range(0,nNvec):
    II = 0
    Idiff = 0
    I1 = trapz_int1(fsin,a,b,Nvec[i])
    I_list.append(I1)
    Idiff = 100 * abs(I1 - Ig0)/Ig0
    err.append(Idiff)


## printing
print("    i        trapezoidal          error %")
for i in range(0, nNvec):
    print ('%7d %.16f %.16f' % (Nvec[i], I_list[i], err[i]))

## trying more complicated functions 
def poly3(x):
    y = 2 + x + x**2 + 3* x**3
    return y

Ig_poly3 = 5.329166666666666e+02
aa = 0
bb = 5
Npoint = 2
Int_poly3 = trapz_int1(poly3,aa,bb,Npoint)


## now let's examine the convergence of the data
Nvec = []
Nvec = [2,4,6,10,12,16,20,30,40,50,60,80,100,200,500,800,1000,10000]
nNvec = len(Nvec)
Ig0  =  Ig_poly3 
err = []
I_list = []
for i in range(0,nNvec):
    II = 0
    Idiff = 0
    I1 = trapz_int1(poly3,aa,bb,Nvec[i])
    I_list.append(I1)
    Idiff = 100 * abs(I1 - Ig0)/Ig0
    err.append(Idiff)


## smooth curve 
# 
# 
Nvec = []
Nvec = np.arange(2,10000,1)
nNvec = len(Nvec)
Ig0  =  Ig_poly3 
err = []
I_list = []
for i in range(0,nNvec):
    II = 0
    Idiff = 0
    I1 = trapz_int1(poly3,aa,bb,Nvec[i])
    I_list.append(I1)
    Idiff = 100 * abs(I1 - Ig0)/Ig0
    err.append(Idiff)


# plotting the difference
plt.plot(Nvec,err)
plt.xlabel("Number of points")
plt.ylabel("err %")
plt.yscale('log')
plt.show()
