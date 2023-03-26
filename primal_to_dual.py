import numpy as np

# Define the primal linear programming problem
# maximize 3x + 4y
# subject to:
#   x + y <= 5
#   2x + y <= 8
#   x >= 0, y >= 0
c = np.array([3, 4])
A = np.array([[1, 1], [2, 1]])
b = np.array([5, 8])
lb = np.array([0, 0])

# Compute the dual linear programming problem
# minimize 5u + 8v
# subject to:
#   u + 2v >= 3
#   u + v >= 4
#   u >= 0, v >= 0
c_dual = b
A_dual = -A.T
b_dual = c
lb_dual = np.array([0, 0])

# Print the primal and dual linear programming problems
print("Primal linear programming problem:")
print("maximize:", c, "x")
print("subject to:")
for i in range(len(A)):
    print(A[i], "x <= ", b[i])
print("x >= ", lb)

print("\nDual linear programming problem:")
print("minimize:", b_dual, "u + ", c_dual, "v")
print("subject to:")
for i in range(len(A_dual)):
    print(A_dual[i], "u + ", A_dual[i][1], "v >= ", c_dual[i])
print("u >= ", lb_dual[0])
print("v >= ", lb_dual[1])
