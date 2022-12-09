from sympy import *
init_printing(pretty_print=true)

x = Symbol('x')

Integral(x**5)

y = Integral(x**5).doit( )
print(y)                        #Passo a passo para resolução da integral