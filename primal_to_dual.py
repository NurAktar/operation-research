import numpy as np

# Read the primal linear programming problem from the input file
with open("inputfordual.txt", "r") as f:
    lines = f.readlines()

c = np.array([int(x) for x in lines[0].split()])
A = np.array([[int(x) for x in line.split()] for line in lines[1:-1]])
b = np.array([int(x) for x in lines[-1].split()])

# Compute the dual linear programming problem
c_dual = b
A_dual = A.T
b_dual = c
lb_dual = np.zeros(len(A_dual))

# Write the dual linear programming problem to the output file
with open("output.txt", "w") as f:
    f.write("minimize: ")
    for i in range(len(c_dual)):
        f.write(str(c_dual[i]) + "w" + str(i+1))
        if i < len(c_dual) - 1:
            f.write(" + ")
    f.write("\nsubject to:\n")
    for i in range(len(A_dual)):
        f.write("    ")
        for j in range(len(A_dual[i])):
            f.write(str(A_dual[i][j]) + "w" + str(j+1))
            if j < len(A_dual[i]) - 1:
                f.write(" + ")
        f.write(" >= " + str(b_dual[i]) + "\n")
    f.write("u >= 0")
