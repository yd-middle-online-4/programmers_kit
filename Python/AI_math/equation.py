from sympy import symbols, Derivative

x = symbols('x')
fx = 2 * x ** 2 + 4 * x + 7

fprime = Derivative(fx ,x).doit()
print(fprime)