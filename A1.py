import sympy as sp
import numpy as np

# Variables
d, theta, r, alpha = sp.symbols('d, theta, r, alpha')

# Transformation matrix using DH parameters
T = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), 0, alpha],
    [sp.sin(theta) * sp.cos(alpha), sp.cos(theta)*sp.cos(alpha), -sp.sin(alpha), -sp.sin(alpha)*d],
    [sp.sin(theta)*sp.sin(alpha), sp.cos(theta)*sp.sin(alpha), sp.cos(alpha), sp.cos(alpha)*d],
    [0, 0, 0, 1]])

# Transformation matrix for the base to the first joint, z0
d_0 = 0 # fixed
theta_0 = sp.symbols('theta_0') # variable
r_0 = 0 # fixed
alpha_0 = 0 # fixed

T_01 = T.subs({d:d_0, theta:theta_0, r:r_0, alpha:alpha_0})

# Transformation matrix for z1
d_1 = sp.symbols('L_12')
theta_1 = sp.symbols('theta_1')
r_1 = 0
alpha_1 = -90*sp.pi/180

T_12 = T.subs({d:d_1, theta:theta_1, r:r_1, alpha:alpha_1})

# Transformation matrix for z2
d_2 = 0
theta_2 = sp.symbols('theta_2')
r_2 = sp.symbols('L_23')
alpha_2 = 0


T_23 = T.subs({d:d_2, theta:theta_2, r:r_2, alpha:alpha_2})

# Transformation matrix for z3
d_3 = 0
theta_3 = sp.symbols('theta_3')
r_3 = sp.symbols('L_34')
alpha_3 = -90*sp.pi/180

T_34 = T.subs({d:d_3, theta:theta_3, r:r_3, alpha:alpha_3})

# Transformation matrix for z4
d_4 = sp.symbols('L_45')
theta_4 = sp.symbols('theta_4')
r_4 = 0
alpha_4 = -90*sp.pi/180

T_45 = T.subs({d:d_4, theta:theta_4, r:r_4, alpha:alpha_4})

# Transformation matrix for z5
d_5 = 0
theta_5 = sp.symbols('theta_5')
r_5 = sp.symbols('L_56')
alpha_5 = -90*sp.pi/180

T_56 = T.subs({d:d_5, theta:theta_5, r:r_5, alpha:alpha_5})

# Transformation matrix for z6
d_6 = sp.symbols('L_67')
theta_6 = sp.symbols('theta_6')
r_6 = 0
alpha_6 = 0

T_67 = T.subs({d:d_6, theta:theta_6, r:r_6, alpha:alpha_6})

# Total transformation matrix
T_07 = T_01 * T_12 * T_23 * T_34 * T_45 * T_56 * T_67
# print(sp.latex(sp.simplify(T_07)))

# Parts of T_07
# rotational elements
r11 = T_07[0,0]
r12 = T_07[0,1]
r13 = T_07[0,2]
r21 = T_07[1,0]
r22 = T_07[1,1]
r23 = T_07[1,2]
r31 = T_07[2,0]
r32 = T_07[2,1]
r33 = T_07[2,2]

# translational elements
px = T_07[0,3]
py = T_07[1,3]
pz = T_07[2,3]

# print elements
print("\n \n \n")
print('r11 = ', sp.latex(sp.simplify(r11)))
#print('r12 = ', sp.latex(sp.simplify(r12)))
#print('r13 = ', sp.latex(sp.simplify(r13)))
#print('r21 = ', sp.latex(sp.simplify(r21)))
#print('r22 = ', sp.latex(sp.simplify(r22)))
#print('r23 = ', sp.latex(sp.simplify(r23)))
#print('r31 = ', sp.latex(sp.simplify(r31)))
#print('r32 = ', sp.latex(sp.simplify(r32)))
#print('r33 = ', sp.latex(sp.simplify(r33)))
#print('px = ', sp.latex(sp.simplify(px)))
#print('py = ', sp.latex(sp.simplify(py)))
#print('pz = ', sp.latex(sp.simplify(pz)))

# replace sin with s and cos with c in strings
print("\n \n \n")
print('r11 = ', sp.latex(sp.simplify(r11)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('r12 = ', sp.latex(sp.simplify(r12)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('r13 = ', sp.latex(sp.simplify(r13)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('r21 = ', sp.latex(sp.simplify(r21)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('r22 = ', sp.latex(sp.simplify(r22)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('r23 = ', sp.latex(sp.simplify(r23)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('r31 = ', sp.latex(sp.simplify(r31)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('r32 = ', sp.latex(sp.simplify(r32)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('r33 = ', sp.latex(sp.simplify(r33)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('px = ', sp.latex(sp.simplify(px)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('py = ', sp.latex(sp.simplify(py)).replace('\sin', 's').replace('\cos', 'c'))
print("\n")
print('pz = ', sp.latex(sp.simplify(pz)).replace('\sin', 's').replace('\cos', 'c'))




