# 3x3 Matrix using a Nested List.
import numpy as np

data = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [11, 22, 33],
        [44, 55, 66],
        [77, 88, 99]
    ],
    [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ],
]

mat3x3 = np.array(data)
print(mat3x3)