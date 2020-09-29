from math import pi as pi

E = 200000  * 10**6
D = 30 * 10**(-3)
a = 600 * 10**(-3)             
M = 400
J = pi*D**4/64
R = M/a

fi_M = 5*M*a/(E*J) - 6*M*a**3/(E*J) + 7/3*M*a/(E*J)
print(fi_M)

u1 = 0.5*a/(E*J)*(a*(R*a - M) - M)
print(u1)
''''''''''''''''''''''''''''''''''''''
