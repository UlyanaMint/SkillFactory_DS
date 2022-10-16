import numpy as np

def get_chess(a):
    chess = np.zeros((a, a), dtype = np.int8)
    print(chess)


get_chess(1)
# array([[0.]])
get_chess(4)
# array([[0., 1., 0., 1.],
#        [1., 0., 1., 0.],
#        [0., 1., 0., 1.],
#        [1., 0., 1., 0.]])