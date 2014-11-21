#Interpolacion de Lagrange
import sympy
from sympy import Symbol
from sympy.parsing.sympy_parser import parse_expr

x = Symbol('x')

Fx = parse_expr(raw_input("Ingrese F(x): "))

n = input("Ingrese el orden del polinomio: ")
Xi = []
Fxi = []
Li = []
P = 0

for i in range(n + 1):
    Xi.append(input("Ingrese X%d: " % i))
    Fxi.append(Fx.subs(x,Xi[i]))
    Li.append(1)
    
for i in range(n + 1):
    for j in range(n + 1):
        if i == j:
            continue
        else:
            Li[i] *= (x - Xi[j])/(Xi[i]- Xi[j]) 
    print "L%d: %r " % ( i, sympy.expand(Li[i]) )

for i in range(n + 1):
    P += (Li[i]*Fxi[i])   
print "El polinomio de Lagrange P%d = %r" % (n,sympy.expand(P))
