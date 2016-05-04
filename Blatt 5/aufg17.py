import numpy as np 
from numpy.linalg import inv, solve
from scipy.linalg import svd

def conditional_number(matrix):
    _, sv, _     = svd(matrix)
    sv_max       = sv[0]

    _, sv_inv, _ = svd(inv(matrix))
    sv_inv_max   = sv_inv[0]

    return sv_max * sv_inv_max

if __name__ == "__main__":

    A_1 = np.array([[3, 1.001],
                    [6, 1.997]])
    
    A_2 = np.array([[3, 1],
                    [0, 2]])

    # 17 (2)
    print("%20s%s%20s" % ("-" * 20, "Aufgabe 17 (2)".center(20), "-" * 20))
    print("Condition number of A_1 is %f" % conditional_number(A_1))
    print("Condition number of A_2 is %f" % conditional_number(A_2))
    
    print("%20s%s%20s" % ("-" * 20, "Aufgabe 17 (3)".center(20), "-" * 20))

    # 17 (3)
    b_1 = np.array([1.999, 4.003])

    b_2 = np.array([2.002, 4])

    for A_i in [A_1, A_2]:
        for b in [b_1, b_2]:
            print("Solving Ax = b with A=\n%s\n and b=%s" % (np.array_str(A_i),
                np.array_str(b)))
            res = solve(A_i, b)
            print("Result = %s\n" % np.array_str(res))
