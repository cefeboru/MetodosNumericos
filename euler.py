from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr

x =Symbol('x')
y = Symbol('y')

Fxy = parse_expr(raw_input('Ingrese F(x): '))


#h = input('Ingrese h: ')
h = 0.5

#Xo = input('Desde X = ')
Xo = 0
#XN = input('Hasta X = ')
XN = 5

#xi = [input('Ingrese Xo')]
#yi = [input('Ingrese Yo')]
xi = [0]
yi = [4]

maxRange = (XN - Xo)/h
e = 5
for i in range(int(maxRange)):
    temp = Fxy.subs(x,xi[i])
    yi.append((yi[i] + h*temp.subs(y,yi[i])).evalf())
    xi.append(xi[i] + h) 
    
for i in range(len(yi)):
    if i == 0:
        print "%r\t%f\t%r" % (i,xi[i],yi[i])
    else:
        print "%r\t%f\t%f" % (i,xi[i],(yi[i].evalf()))
