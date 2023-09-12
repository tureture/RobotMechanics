import sympy as sp
import numpy as np

# Variables
d, theta, r, alpha = sp.symbols('d, theta, r, alpha')

# Transformation matrix using DH parameters
T = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), 0, alpha],
    [sp.sin(theta) * sp.cos(alpha), sp.cos(theta)*sp.cos(alpha), -sp.sin(alpha), -sp.sin(alpha)*d],
    [sp.sin(theta)*sp.sin(alpha), sp.cos(theta)*sp.sin(alpha), sp.cos(alpha), sp.cos(alpha)*d],
    [0, 0, 0, 1]])

# Transformation matrix for the first joint, z0
# d_0 = 0.5 # fixed
d_0 = sp.symbols('d_0') # fixed
# theta_0 = sp.pi/2 # variable
theta_0 = sp.symbols('theta_0') # variable
r_0 = 0 # fixed
alpha_0 = sp.pi/2 # fixed

T_01 = T.subs({d:d_0, theta:theta_0, r:r_0, alpha:alpha_0})

# Transformation matrix for the second joint, z1
d_1 = 0 # fixed
# theta_1 = sp.pi/2 # variable
theta_1 = sp.symbols('theta_1') # variable
# r_1 = 1 # fixed
r_1 = sp.symbols('r_1') # fixed
alpha_1 = 0 # fixed

T_12 = T.subs({d:d_1, theta:theta_1, r:r_1, alpha:alpha_1})

# Transformation matrix for the third joint, z2
d_2 = 0 # fixed
# theta_2 = sp.pi/2 # variable
theta_2 = sp.symbols('theta_2') # variable
r_2 = 1 # fixed
alpha_2 = -sp.pi/2 # fixed

T_23 = T.subs({d:d_2, theta:theta_2, r:r_2, alpha:alpha_2})

# Transformation matrix for the fourth joint, z3
# d_3 = 1 # fixed
d_3 = sp.symbols('d_3') # fixed
# theta_3 = 0 # variable
theta_3 = sp.symbols('theta_3') # variable
r_3 = 0 # fixed
alpha_3 = sp.pi/2 # fixed

T_34 = T.subs({d:d_3, theta:theta_3, r:r_3, alpha:alpha_3})

# Transformation matrix for the fifth joint, z4
d_4 = 0 # fixed
# theta_4 = sp.pi/2 # variable
theta_4 = sp.symbols('theta_4') # variable
# r_4 = 1 # fixed
r_4 = sp.symbols('r_4') # fixed
alpha_4 = sp.pi/2 # fixed

T_45 = T.subs({d:d_4, theta:theta_4, r:r_4, alpha:alpha_4})

# Transformation matrix for the sixth joint, z5
d_5 = 0 # fixed
# theta_5 = 0 # variable
theta_5 = sp.symbols('theta_5') # variable
r_5 = 0 # fixed
alpha_5 = sp.pi/2 # fixed

T_56 = T.subs({d:d_5, theta:theta_5, r:r_5, alpha:alpha_5})

# Total transformation matrix
T_06 = T_01 * T_12 * T_23 * T_34 * T_45 * T_56
print(sp.latex(sp.simplify(T_06)))


