import numpy as np
from math import sqrt


def dot_prod(m1, m2):
    r = np.trace(m1.T.dot(m2))
    return r


def norm(m):
    r = sqrt(dot_prod(m, m))
    return r


if __name__ == "__main__":

    # # part (1)
    # v_1 = np.array([[1,2], [1,0]])
    # v_2 = np.array([[-1,0], [1,0]])
    # v_3 = np.array([[-2,1], [0,1]])

    # w_1 = v_1 / norm(v_1)
    # w_2_tmp = v_2 - dot_prod(v_2,w_1) * w_1
    # w_2 = w_2_tmp / norm(w_2_tmp)
    # w_3_tmp = v_3 - dot_prod(v_3,w_1) * w_1 - dot_prod(v_3, w_2) * w_2
    # w_3 = w_3_tmp / norm(w_3_tmp)

    # print("w_1 = \n%s" % np.array_str(w_1))
    # print("w_2 = \n%s" % np.array_str(w_2))
    # print("w_3 = \n%s" % np.array_str(w_3))

    # part (2)
    v_1 = np.array([[1, 0], [0, 1]])
    v_2 = np.array([[0, 1], [1, 0]])
    v_3 = np.array([[1, 1], [0, 0]])
    v_4 = np.array([[0, 0], [1, 1]])

    w_1 = v_1 / norm(v_1)
    w_2_tmp = v_2 - dot_prod(v_2, w_1) * w_1
    w_2 = w_2_tmp / norm(w_2_tmp)
    w_3_tmp = v_3 - dot_prod(v_3, w_1) * w_1 - dot_prod(v_3, w_2) * w_2
    w_3 = w_3_tmp / norm(w_3_tmp)
    w_4_tmp = v_4 - dot_prod(v_4, w_1) * w_1 - dot_prod(
        v_4, w_2) * w_2 - dot_prod(v_4, w_3) * w_3
    w_4 = w_4_tmp / norm(w_4_tmp)

    print("w_1 = \n%s" % np.array_str(w_1))
    print("w_2 = \n%s" % np.array_str(w_2))
    print("w_3 = \n%s" % np.array_str(w_3))
    print("w_4 = \n%s" % np.array_str(w_4))
