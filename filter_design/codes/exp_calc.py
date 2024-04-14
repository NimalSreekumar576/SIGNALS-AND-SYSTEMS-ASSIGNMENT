from sympy import symbols, simplify

# Define symbolic variable s
s = symbols(' s ')

# Constants
omega0_val = 0.4895
B_val =0.098


# Given roots
s1 = -0.1621 - 1.0033j
s2 = -0.3913 - 0.4156j 
s3 =-0.3913 + 0.4156j
s4 = -0.1621 + 1.0033j 

# Define the given polynomial expression
polynomial_expr = 0.3125/ ((s - s1) * (s - s2) * (s - s3) * (s - s4))

# Simplify the expression
simplified_expr = simplify(polynomial_expr)

# Print the simplified expression
print("Simplified Polynomial in terms of s:")
print(simplified_expr)
