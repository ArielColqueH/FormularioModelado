import sympy

tempprom=37
tempamb=15
temphdesp=33.9
tempinit=34.5

t, k = sympy.symbols('t k')
y = sympy.Function('y')

f = k*(y(t) - tempamb)
sympy.Eq(y(t).diff(t), f)

edo_sol = sympy.dsolve(y(t).diff(t) - f)


ics = {y(0): tempinit}

C_eq = sympy.Eq(edo_sol.lhs.subs(t, 0).subs(ics), edo_sol.rhs.subs(t, 0))

C = sympy.solve(C_eq)[0]

eq = sympy.Eq(y(t), C * sympy.E**(k*t) + tempamb)

ics = {y(1): temphdesp}
k_eq = sympy.Eq(eq.lhs.subs(t, 1).subs(ics), eq.rhs.subs(t, 1))
kn = round(sympy.solve(k_eq)[0], 4)

hmuerte = sympy.Eq(tempprom, C * sympy.E**(kn*t) + tempamb)

t = round(sympy.solve(hmuerte)[0],2)

h, m = divmod(t*-60, 60)
print("Pasaron Aproximadamente:")
print ("%d horas, %d minutos" % (h, m))
print("Desde que ocurrio el crimen")