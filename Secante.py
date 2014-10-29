from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations
from sympy.parsing.sympy_parser import implicit_multiplication_application
from sympy import Symbol
from sympy.solvers import solve
from sympy import diff
from math import ceil, floor, log10

transformations = (standard_transformations + (implicit_multiplication_application,))

x = Symbol('x')

expresion = raw_input("Ingrese una expresion: ")

expresion = parse_expr(expresion, transformations=transformations)

N = input("ingrese el numero de iteraciones: ")

tol = input("ingrese la tolerancia: ")

def evalPol(value):
    resultado = 0.00
    resultado = expresion.subs(x, value)
    return float(resultado)

P = [2,3]

print "N         Pn               P(n+2)"
for i in range(N):
    P.append( P[i+1] - (evalPol(P[i+1])*(P[i+1]-P[i])/( evalPol(P[i+1]) - evalPol(P[i])) )) 
    print "%d         %f         %f" % (i, P[i], P[i+2])
