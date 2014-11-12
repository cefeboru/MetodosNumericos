#from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations
from sympy.parsing.sympy_parser import implicit_multiplication_application
from sympy import Symbol
from sympy import diff

transformations = (standard_transformations + (implicit_multiplication_application,))

x = Symbol('x')
y = Symbol('y')

f1 = 2*x**2 + y**2 -8
f2 = x**2 - y**2 + x*y - 4
#f1 = raw_input("Ingrese F1(x,y): ")
#f2 = raw_input("Ingrese F2(x,y): ")

#f1 = parse_expr(f1, transformations=transformations)
#f2 = parse_expr(f2, transformations=transformations)


Xs = [input("Ingrese X0: ")]
Ys = [input("Ingrese Y0: ")]

N = input("Ingrese el numero de iteraciones: ")

f1x = diff(f1, x)
f1y = diff(f1, y)
f2x = diff(f2, x)
f2y = diff(f2, y) 

a=0
b=0
c=0
d=0

for i in range(N):
    
    if "x" not in str(f1x.args):
        a = f1x.subs(y, Ys[i])
    elif "y" not in str(f1x.args):
        a = f1x.subs(x, Xs[i])
    else:
        a = f1x.subs([(x,Xs[i]),(y,Ys[i])])
        
    if "x" not in str(f1y.args):
        b = f1y.subs(y, Ys[i])
    elif "y" not in str(f1y.args):
        b = f1y.subs(x, Xs[i])
    else:
        b = f1y.subs([(x,Xs[i]),(y,Ys[i])])
        
    if "x" not in str(f2x.args):
        c = f2x.subs(y, Ys[i])
    elif "y" not in str(f2x.args):
        c = f2x.subs(x, Xs[i])
    else:
        c = f2x.subs([(x,Xs[i]),(y,Ys[i])])
        
    if "x" not in str(f2y.args):
        c = f2y.subs(y, Ys[i])
    elif "y" not in str(f2y.args):
        c = f2y.subs(x, Xs[i])
    else:
        c = f2y.subs([(x,Xs[i]),(y,Ys[i])])
        
    Xs.append(Xs[i] - 1/(a*d - c*b))
