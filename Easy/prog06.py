# Adding 2 matrices using numpy.

# Randomly generating 2 2x2 matrices with 2-digts and adding them.

import numpy as np

low, high = 0, 100
test_order = (2, 2)

mat1 = np.random.randint(low, high, test_order, dtype="int32")
print(f"\nMat1 : \n",mat1)
mat2 = np.random.randint(low, high, test_order, dtype="int32")
print(f"\nMat2 : \n",mat2)

res_mat = mat1 + mat2
print(f"\nRes_Mat : \n",res_mat)
