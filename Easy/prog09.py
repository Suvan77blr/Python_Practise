import numpy as np

def getMatrixSum(matrix):
    sum_total = 0

    for row in matrix:
        for num in row:
            sum_total += num

    return sum_total
    # Alternatively.
    # sum_total = matrix.sum()
# end-function.

def main():
    # Generating a random matrix order between 1 and 5.
    range_low, range_high = 1, 5
    order = ((range_high - range_low + 1) * np.random.random_sample(2) + 1).astype(int)
    print(f"Order : {order[0]} x {order[1]}")

    # Generating a random 2d matrix of obtained 'order', of 2 digits.
    mat2d = np.random.randint(10, 100, size=order, dtype="int32")
    print(f"2D Matrix : \n", mat2d)

    sum_of_elements = getMatrixSum(mat2d)

    print(f"Sum : {sum_of_elements}")

# Calling the main function.
main()