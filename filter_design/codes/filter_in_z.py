import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 2.88e-5 * s**4 / (s**8 + 0.108*s**7 + 0.973*s**6 + 0.075*s**5 + 0.351*s**4 +0.018*s**3 + 0.055*s**2 + 0.001*s + 0.003)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


