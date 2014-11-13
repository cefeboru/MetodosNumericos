from sympy.parsing.sympy_parser import parse_expr
import numpy
from numpy import linalg 
from sympy.parsing.sympy_parser import standard_transformations
from sympy.parsing.sympy_parser import implicit_multiplication_application
from sympy import Symbol
from sympy import diff

transformations = (standard_transformations + (implicit_multiplication_application,))

x = Symbol('x')
y = Symbol('y')

f1 = raw_input("Ingrese F1(x,y): ")
f2 = raw_input("Ingrese F2(x,y): ")
tolerancia = input("Ingrese la tolerancia: ")

f1 = parse_expr(f1, transformations=transformations)
f2 = parse_expr(f2, transformations=transformations)


X = [input("Ingrese X0: ")]
Y = [input("Ingrese Y0: ")]

f1x = diff(f1, x)
f1y = diff(f1, y)
f2x = diff(f2, x)
f2y = diff(f2, y) 

a=0
b=0
c=0
d=0

def getA(xi,yi):
    if "x" not in str(f1x.args):
        return (f1x.subs(y, yi))
    elif "y" not in str(f1x.args):
        return (f1x.subs(x, xi))
    else:
        return (f1x.subs([(x,xi),(y,yi)]))
        
def getB(xi,yi):
    if "x" not in str(f1y.args):
        return (f1y.subs(y, yi))
    elif "y" not in str(f1y.args):
        return (f1y.subs(x, xi))
    else:
        return (f1y.subs([(x,xi),(y,yi)]))
        
def getC(xi,yi):
    if "x" not in str(f2x.args):
        return (f2x.subs(y, yi))
    elif "y" not in str(f2x.args):
        return (f2x.subs(x, xi))
    else:
        return (f2x.subs([(x,xi),(y,yi)]))
        
def getD(xi,yi):
    if "x" not in str(f2y.args):
        return (f2y.subs(y, yi))
    elif "y" not in str(f2y.args):
        return (f2y.subs(x, xi))
    else:
        return (f2y.subs([(x,xi),(y,yi)]))
    
print "i\tXi\t\tYi\t\tF1(xi)\t\tF2(xi)"

for i in range(100):
    xi = X[i]
    yi = Y[i]
        
    a = getA(xi, yi)
    b = getB(xi, yi)
    c = getC(xi, yi)
    d = getD(xi, yi)
    
    jacobiano = linalg.inv( numpy.array([[a, b], [c, d]]) )
    f1e = f1.subs([(x,xi),(y,yi)])
    f2e = f2.subs([(x,xi),(y,yi)])
    Fs = numpy.array([f1e,f2e]) 
    XI = numpy.array([X[i],Y[i]])
    
    Xplus = XI - numpy.dot(jacobiano,Fs)
    X.append(Xplus[0])
    Y.append(Xplus[1])
    print "%d\t%f\t%f\t%f\t%f" % (i,xi,yi,f1e,f2e)
    if (abs(f1e) < tolerancia) and (abs(f2e) < tolerancia):
        break
