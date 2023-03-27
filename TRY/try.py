from sympy import symbols, Eq, solve

a, b, c = symbols('a b c')
eq = Eq(2*a + 5*b + 15*c, 12)
sol = solve(eq)
print(sol)