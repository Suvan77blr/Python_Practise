import numpy as np

# Generating a random matrix order between 1 and 5.
range_low, range_high = 1, 5
order = ((range_high - range_low + 1) * np.random.random_sample(2) + 1).astype(int)

# Generating a random 2d matrix of obtained 'order', of 2 digits.
mat2d = np.random.randint(10, 100, size=order, dtype="int32")

# Variables to store highest and lowest numbers.
high, low = [ mat2d[0][0] ]*2

for row in mat2d:
   for num in row:
       if num > high:
           high = num
       if num < low:
           low = num
   # end-inner-for
# end-outer-for

print(f"Order : {order[0]} x {order[1]}")
print(f"2D Matrix : \n", mat2d)

print(f"\nHighest: {high}")
print(f"Lowest: {low}")