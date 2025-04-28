# Creating ID matrix of order 4. => generic to any 'n'
import numpy as np

n = int(input("Enter the order of ID matrix required : "))
id_mat_NxN = np.identity(n, dtype="int32")
print(id_mat_NxN)